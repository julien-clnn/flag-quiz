import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [currentFlag, setCurrentFlag] = useState(null);
  const [userGuess, setUserGuess] = useState('');
  const [score, setScore] = useState(0);
  const [loading, setLoading] = useState(true);
  const [allCountries, setAllCountries] = useState([]);
  // Track current suggestions and index
  const [currentSuggestions, setCurrentSuggestions] = useState([]);
  const [suggestionIndex, setSuggestionIndex] = useState(0);

  const API_BASE_URL = 'http://127.0.0.1:5000';

  const fetchAllCountries = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/countries`);
      setAllCountries(response.data);
    } catch (error) {
      console.error('Error fetching countries:', error);
    }
  };

  const fetchNewFlag = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/flag`);
      const flagData = {
        ...response.data,
        flag_url: `${API_BASE_URL}/flags/${response.data.flag_path}`
      };
      setCurrentFlag(flagData);
    } catch (error) {
      console.error('Error fetching flag:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNewFlag();
    fetchAllCountries();
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (userGuess.toLowerCase() === currentFlag?.name.toLowerCase()) {
      setScore(prevScore => prevScore + 1);
      setUserGuess('');
      fetchNewFlag();
    } else {
      setUserGuess('');
    }
    // Reset suggestions state
    setCurrentSuggestions([]);
    setSuggestionIndex(0);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      
      if (userGuess) {
        // If we don't have current suggestions, get them
        if (currentSuggestions.length === 0) {
          const matches = allCountries
            .filter(country => country.toLowerCase().startsWith(userGuess.toLowerCase()))
            .sort(); // Sort alphabetically
          
          if (matches.length > 0) {
            setCurrentSuggestions(matches);
            setUserGuess(matches[0]); // Set first match
          }
        }
        // If we already have suggestions, cycle through them
        else {
          const nextIndex = (suggestionIndex + 1) % currentSuggestions.length;
          setSuggestionIndex(nextIndex);
          setUserGuess(currentSuggestions[nextIndex]);
        }
      }
    } else if (e.key !== 'Tab') {
      // Reset suggestions if any other key is pressed
      setCurrentSuggestions([]);
      setSuggestionIndex(0);
    }
  };

  return (
    <div className="flag-quiz">
      <h1>Flag Quiz Game</h1>
      <p>Current Score: {score}</p>
      
      {loading ? (
        <p>Loading...</p>
      ) : currentFlag ? (
        <>
          <img 
            src={currentFlag.flag_url} 
            alt="Guess this flag" 
            style={{ 
              maxWidth: '300px', 
              border: '1px solid #ccc',
              marginBottom: '20px'
            }}
          />
          <form onSubmit={handleSubmit} style={{ marginTop: '20px' }}>
            <input
              type="text"
              value={userGuess}
              onChange={(e) => setUserGuess(e.target.value)}
              onKeyDown={handleKeyDown}
              placeholder="Enter country name"
              style={{ 
                padding: '10px',
                width: '300px',
                fontSize: '16px',
                borderRadius: '5px',
                border: '1px solid #ccc'
              }}
              autoFocus
            />
          </form>
        </>
      ) : (
        <p>Error loading flag</p>
      )}
    </div>
  );
}

export default App;