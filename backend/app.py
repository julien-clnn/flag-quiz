from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import random
import os

app = Flask(__name__)
CORS(app)

REGIONS = {
    "Europe": [
        "France", "Germany", "Italy", "United Kingdom", "Spain", "Portugal", "Netherlands",
        "Belgium", "Switzerland", "Austria", "Sweden", "Norway", "Finland", "Denmark",
        "Poland", "Ukraine", "Greece", "Romania", "Hungary", "Czech Republic"
    ],
    "North America": ["United States", "Canada", "Mexico"],
    "South America": [
        "Brazil", "Argentina", "Chile", "Colombia", "Peru", "Venezuela", 
        "Uruguay", "Paraguay", "Bolivia", "Ecuador"
    ],
    "Asia": [
        "China", "Japan", "South Korea", "India", "Vietnam", "Thailand", 
        "Indonesia", "Malaysia", "Philippines", "Singapore"
    ],
    "Africa": [
        "South Africa", "Egypt", "Morocco", "Nigeria", "Kenya", "Ethiopia",
        "Ghana", "Senegal", "Tanzania", "Uganda"
    ],
    "Oceania": [
        "Australia", "New Zealand", "Fiji", "Papua New Guinea"
    ]
}

# Load flags data
try:
    with open('flags/flags_metadata.json', 'r', encoding='utf-8') as f:
        FLAGS = json.load(f)
        for flag in FLAGS:
            flag['flag_path'] = os.path.basename(flag['flag_path'])
except FileNotFoundError:
    print("Flags metadata file not found")
    FLAGS = []

@app.route('/flag', methods=['GET'])
def get_random_flag():
    if not FLAGS:
        return jsonify({"error": "No flags available"}), 404
    
    flag = random.choice(FLAGS)
    return jsonify({
        "name": flag['name'],
        "flag_path": flag['flag_path']
    })

@app.route('/flag/<region>', methods=['GET'])
def get_random_region_flag(region):
    if region not in REGIONS:
        return jsonify({"error": "Invalid region"}), 400
        
    region_flags = [
        flag for flag in FLAGS 
        if flag['name'] in REGIONS[region]
    ]
    
    if not region_flags:
        return jsonify({"error": f"No flags available for {region}"}), 404
    
    flag = random.choice(region_flags)
    return jsonify({
        "name": flag['name'],
        "flag_path": flag['flag_path']
    })

@app.route('/regions', methods=['GET'])
def get_regions():
    return jsonify(list(REGIONS.keys()))

@app.route('/flags/<filename>')
def serve_flag(filename):
    return send_from_directory('flags', filename)

@app.route('/countries', methods=['GET'])
def get_countries():
    countries = [flag['name'] for flag in FLAGS]
    return jsonify(countries)

if __name__ == '__main__':
    app.run(debug=True, port=5000)