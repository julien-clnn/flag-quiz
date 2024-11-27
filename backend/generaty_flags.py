import os
import json
import requests

def download_flags():
    countries = [
        {"name": "France", "code": "fr"},
        {"name": "United States", "code": "us"},
        {"name": "United Kingdom", "code": "gb"},
        {"name": "Germany", "code": "de"},
        {"name": "Italy", "code": "it"},
        {"name": "Japan", "code": "jp"},
        {"name": "Canada", "code": "ca"},
        {"name": "Australia", "code": "au"},
        {"name": "Brazil", "code": "br"},
        {"name": "China", "code": "cn"},
        {"name": "India", "code": "in"},
        {"name": "Russia", "code": "ru"},
        {"name": "Spain", "code": "es"},
        {"name": "Mexico", "code": "mx"},
        {"name": "South Korea", "code": "kr"}
    ]

    flags_data = []
    flags_folder = 'flags'
    os.makedirs(flags_folder, exist_ok=True)

    for country in countries:
        # Utiliser flagcdn.com pour les drapeaux
        flag_url = f"https://flagcdn.com/w320/{country['code'].lower()}.png"
        
        try:
            # Télécharger le drapeau
            response = requests.get(flag_url)
            if response.status_code == 200:
                # Sauvegarder le drapeau
                filename = f"{flags_folder}/{country['name'].lower().replace(' ', '_')}_flag.png"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                
                # Ajouter aux données
                flags_data.append({
                    "name": country['name'],
                    "flag_path": filename,
                    "flag_code": country['code']
                })
                print(f"Téléchargé le drapeau de {country['name']}")
            else:
                print(f"Impossible de télécharger le drapeau de {country['name']}")
        
        except Exception as e:
            print(f"Erreur pour {country['name']}: {e}")

    # Sauvegarder les métadonnées
    with open(f'{flags_folder}/flags_metadata.json', 'w') as f:
        json.dump(flags_data, f, indent=4)

    print(f"Téléchargement terminé. {len(flags_data)} drapeaux sauvegardés.")

if __name__ == "__main__":
    download_flags()