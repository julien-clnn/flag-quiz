import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [currentFlag, setCurrentFlag] = useState(null);
  const [userGuess, setUserGuess] = useState('');
  const [loading, setLoading] = useState(true);
  const [allCountries, setAllCountries] = useState([]);
  const [currentSuggestions, setCurrentSuggestions] = useState([]);
  const [suggestionIndex, setSuggestionIndex] = useState(0);
  const [showDropdown, setShowDropdown] = useState(false);
  const [regions, setRegions] = useState([]);
  const [selectedRegion, setSelectedRegion] = useState('all');

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
      const endpoint = selectedRegion === 'all' ? '/flag' : `/flag/${selectedRegion}`;
      const response = await axios.get(`${API_BASE_URL}${endpoint}`);
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

  const handleSubmit = (e) => {
    e.preventDefault();
    if (userGuess.toLowerCase() === currentFlag?.name.toLowerCase()) {
      setUserGuess('');
      fetchNewFlag();
    } else {
      setUserGuess('');
    }
    setCurrentSuggestions([]);
    setSuggestionIndex(0);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Tab') {
      e.preventDefault();
      if (userGuess) {
        if (currentSuggestions.length === 0) {
          const matches = allCountries
            .filter(country => country.toLowerCase().startsWith(userGuess.toLowerCase()))
            .sort();
          if (matches.length > 0) {
            setCurrentSuggestions(matches);
            setUserGuess(matches[0]);
          }
        } else {
          const nextIndex = (suggestionIndex + 1) % currentSuggestions.length;
          setSuggestionIndex(nextIndex);
          setUserGuess(currentSuggestions[nextIndex]);
        }
      }
    } else if (e.key !== 'Tab') {
      setCurrentSuggestions([]);
      setSuggestionIndex(0);
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        const regionsResponse = await axios.get(`${API_BASE_URL}/regions`);
        setRegions(regionsResponse.data);
      } catch (error) {
        console.error('Error fetching regions:', error);
      }
    };
    fetchData();
  }, []);

  useEffect(() => {
    fetchNewFlag();
    fetchAllCountries();
  }, [selectedRegion]);

  return (
    <div className="app-container">
      <nav className="navbar">
        <div className="nav-brand">&#127758; Flag Quiz</div>
        <div className="nav-modes">
          <div className="dropdown">
            <button 
              className="mode-button"
              onClick={() => setShowDropdown(!showDropdown)}
            >
              {selectedRegion === 'all' ? 'All Flags' : selectedRegion}
              <span className="dropdown-arrow">▼</span>
            </button>
            {showDropdown && (
              <div className="dropdown-menu">
                <div
                  className="dropdown-item"
                  onClick={() => {
                    setSelectedRegion('all');
                    setShowDropdown(false);
                  }}
                >
                  All Flags
                </div>
                {regions.map(region => (
                  <div
                    key={region}
                    className="dropdown-item"
                    onClick={() => {
                      setSelectedRegion(region);
                      setShowDropdown(false);
                    }}
                  >
                    {region}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </nav>

      <div className="flag-quiz">
      {loading ? (
          <p>Loading...</p>
        ) : currentFlag ? (
          <>
            <div className="flag-container">
              <img 
                src={currentFlag.flag_url} 
                alt="Guess this flag" 
              />
            </div>
            <form onSubmit={handleSubmit}>
              <input
                type="text"
                value={userGuess}
                onChange={(e) => setUserGuess(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder="Enter country name"
                autoFocus
              />
            </form>
          </>
        ) : (
          <p>Error loading flag</p>
        )}
      </div>
    </div>
  );
}

export default App;