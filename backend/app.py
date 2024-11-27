import json
import os
import random
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permettre les requêtes cross-origin

# Charger les métadonnées des drapeaux
try:
    with open('flags/flags_metadata.json', 'r', encoding='utf-8') as f:
        FLAGS = json.load(f)
except FileNotFoundError:
    print("Fichier de métadonnées de drapeaux non trouvé. Exécutez d'abord le script de téléchargement.")
    FLAGS = []

@app.route('/flag', methods=['GET'])
def get_random_flag():
    if not FLAGS:
        return jsonify({"error": "Aucun drapeau disponible"}), 404
    
    # Sélectionner un drapeau au hasard
    flag = random.choice(FLAGS)
    
    # Renvoyer le chemin complet pour que le navigateur puisse l'afficher
    return jsonify({
        "name": flag['name'],
        "flag_url": f"http://localhost:5000/flags/{os.path.basename(flag['flag_path'])}"
    })

@app.route('/flags/<path:filename>')
def serve_flag(filename):
    return send_from_directory('flags', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)