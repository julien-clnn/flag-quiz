from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json
import random
import os

app = Flask(__name__)
CORS(app)

# Load flags data
try:
    with open('flags/flags_metadata.json', 'r', encoding='utf-8') as f:
        FLAGS = json.load(f)
except FileNotFoundError:
    print("Flags metadata file not found")
    FLAGS = []

@app.route('/flag', methods=['GET'])
def get_random_flag():
    if not FLAGS:
        return jsonify({"error": "No flags available"}), 404
    
    flag = random.choice(FLAGS)
    # Get just the filename from the full path
    filename = os.path.basename(flag['flag_path'])
    
    return jsonify({
        "name": flag['name'],
        # Send only the filename, not the full path
        "flag_path": filename
    })

@app.route('/flags/<filename>')
def serve_flag(filename):
    # Serve files from the flags directory
    print(f"Serving flag: {filename}")  # Debug print
    return send_from_directory('flags', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)