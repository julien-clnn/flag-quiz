import os
import json
import requests

def download_flags():
    # Liste complète des pays avec leurs codes ISO
    countries = [
        {"name": "Afghanistan", "code": "af"}, {"name": "Albania", "code": "al"},
        {"name": "Algeria", "code": "dz"}, {"name": "Andorra", "code": "ad"},
        {"name": "Angola", "code": "ao"}, {"name": "Argentina", "code": "ar"},
        {"name": "Armenia", "code": "am"}, {"name": "Australia", "code": "au"},
        {"name": "Austria", "code": "at"}, {"name": "Azerbaijan", "code": "az"},
        {"name": "Bahamas", "code": "bs"}, {"name": "Bahrain", "code": "bh"},
        {"name": "Bangladesh", "code": "bd"}, {"name": "Barbados", "code": "bb"},
        {"name": "Belarus", "code": "by"}, {"name": "Belgium", "code": "be"},
        {"name": "Belize", "code": "bz"}, {"name": "Benin", "code": "bj"},
        {"name": "Bhutan", "code": "bt"}, {"name": "Bolivia", "code": "bo"},
        {"name": "Bosnia and Herzegovina", "code": "ba"}, {"name": "Botswana", "code": "bw"},
        {"name": "Brazil", "code": "br"}, {"name": "Brunei", "code": "bn"},
        {"name": "Bulgaria", "code": "bg"}, {"name": "Burkina Faso", "code": "bf"},
        {"name": "Burundi", "code": "bi"}, {"name": "Cambodia", "code": "kh"},
        {"name": "Cameroon", "code": "cm"}, {"name": "Canada", "code": "ca"},
        {"name": "Cape Verde", "code": "cv"}, {"name": "Central African Republic", "code": "cf"},
        {"name": "Chad", "code": "td"}, {"name": "Chile", "code": "cl"},
        {"name": "China", "code": "cn"}, {"name": "Colombia", "code": "co"},
        {"name": "Comoros", "code": "km"}, {"name": "Costa Rica", "code": "cr"},
        {"name": "Croatia", "code": "hr"}, {"name": "Cuba", "code": "cu"},
        {"name": "Cyprus", "code": "cy"}, {"name": "Czech Republic", "code": "cz"},
        {"name": "Denmark", "code": "dk"}, {"name": "Djibouti", "code": "dj"},
        {"name": "Dominican Republic", "code": "do"}, {"name": "Ecuador", "code": "ec"},
        {"name": "Egypt", "code": "eg"}, {"name": "El Salvador", "code": "sv"},
        {"name": "Estonia", "code": "ee"}, {"name": "Ethiopia", "code": "et"},
        {"name": "Fiji", "code": "fj"}, {"name": "Finland", "code": "fi"},
        {"name": "France", "code": "fr"}, {"name": "Gabon", "code": "ga"},
        {"name": "Gambia", "code": "gm"}, {"name": "Georgia", "code": "ge"},
        {"name": "Germany", "code": "de"}, {"name": "Ghana", "code": "gh"},
        {"name": "Greece", "code": "gr"}, {"name": "Grenada", "code": "gd"},
        {"name": "Guatemala", "code": "gt"}, {"name": "Guinea", "code": "gn"},
        {"name": "Guyana", "code": "gy"}, {"name": "Haiti", "code": "ht"},
        {"name": "Honduras", "code": "hn"}, {"name": "Hungary", "code": "hu"},
        {"name": "Iceland", "code": "is"}, {"name": "India", "code": "in"},
        {"name": "Indonesia", "code": "id"}, {"name": "Iran", "code": "ir"},
        {"name": "Iraq", "code": "iq"}, {"name": "Ireland", "code": "ie"},
        {"name": "Israel", "code": "il"}, {"name": "Italy", "code": "it"},
        {"name": "Jamaica", "code": "jm"}, {"name": "Japan", "code": "jp"},
        {"name": "Jordan", "code": "jo"}, {"name": "Kazakhstan", "code": "kz"},
        {"name": "Kenya", "code": "ke"}, {"name": "Kuwait", "code": "kw"},
        {"name": "Kyrgyzstan", "code": "kg"}, {"name": "Laos", "code": "la"},
        {"name": "Latvia", "code": "lv"}, {"name": "Lebanon", "code": "lb"},
        {"name": "Lesotho", "code": "ls"}, {"name": "Liberia", "code": "lr"},
        {"name": "Libya", "code": "ly"}, {"name": "Liechtenstein", "code": "li"},
        {"name": "Lithuania", "code": "lt"}, {"name": "Luxembourg", "code": "lu"},
        {"name": "Madagascar", "code": "mg"}, {"name": "Malawi", "code": "mw"},
        {"name": "Malaysia", "code": "my"}, {"name": "Maldives", "code": "mv"},
        {"name": "Mali", "code": "ml"}, {"name": "Malta", "code": "mt"},
        {"name": "Mauritania", "code": "mr"}, {"name": "Mauritius", "code": "mu"},
        {"name": "Mexico", "code": "mx"}, {"name": "Moldova", "code": "md"},
        {"name": "Monaco", "code": "mc"}, {"name": "Mongolia", "code": "mn"},
        {"name": "Montenegro", "code": "me"}, {"name": "Morocco", "code": "ma"},
        {"name": "Mozambique", "code": "mz"}, {"name": "Myanmar", "code": "mm"},
        {"name": "Namibia", "code": "na"}, {"name": "Nepal", "code": "np"},
        {"name": "Netherlands", "code": "nl"}, {"name": "New Zealand", "code": "nz"},
        {"name": "Nicaragua", "code": "ni"}, {"name": "Niger", "code": "ne"},
        {"name": "Nigeria", "code": "ng"}, {"name": "North Korea", "code": "kp"},
        {"name": "Norway", "code": "no"}, {"name": "Oman", "code": "om"},
        {"name": "Pakistan", "code": "pk"}, {"name": "Panama", "code": "pa"},
        {"name": "Papua New Guinea", "code": "pg"}, {"name": "Paraguay", "code": "py"},
        {"name": "Peru", "code": "pe"}, {"name": "Philippines", "code": "ph"},
        {"name": "Poland", "code": "pl"}, {"name": "Portugal", "code": "pt"},
        {"name": "Qatar", "code": "qa"}, {"name": "Romania", "code": "ro"},
        {"name": "Russia", "code": "ru"}, {"name": "Rwanda", "code": "rw"},
        {"name": "Saudi Arabia", "code": "sa"}, {"name": "Senegal", "code": "sn"},
        {"name": "Serbia", "code": "rs"}, {"name": "Sierra Leone", "code": "sl"},
        {"name": "Singapore", "code": "sg"}, {"name": "Slovakia", "code": "sk"},
        {"name": "Slovenia", "code": "si"}, {"name": "Somalia", "code": "so"},
        {"name": "South Africa", "code": "za"}, {"name": "South Korea", "code": "kr"},
        {"name": "South Sudan", "code": "ss"}, {"name": "Spain", "code": "es"},
        {"name": "Sri Lanka", "code": "lk"}, {"name": "Sudan", "code": "sd"},
        {"name": "Sweden", "code": "se"}, {"name": "Switzerland", "code": "ch"},
        {"name": "Syria", "code": "sy"}, {"name": "Taiwan", "code": "tw"},
        {"name": "Tajikistan", "code": "tj"}, {"name": "Tanzania", "code": "tz"},
        {"name": "Thailand", "code": "th"}, {"name": "Togo", "code": "tg"},
        {"name": "Tunisia", "code": "tn"}, {"name": "Turkey", "code": "tr"},
        {"name": "Turkmenistan", "code": "tm"}, {"name": "Uganda", "code": "ug"},
        {"name": "Ukraine", "code": "ua"}, {"name": "United Arab Emirates", "code": "ae"},
        {"name": "United Kingdom", "code": "gb"}, {"name": "United States", "code": "us"},
        {"name": "Uruguay", "code": "uy"}, {"name": "Uzbekistan", "code": "uz"},
        {"name": "Venezuela", "code": "ve"}, {"name": "Vietnam", "code": "vn"},
        {"name": "Yemen", "code": "ye"}, {"name": "Zambia", "code": "zm"},
        {"name": "Zimbabwe", "code": "zw"}
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
                print(f"Downloaded flag of {country['name']}")
            else:
                print(f"Could not download flag of {country['name']}")
        
        except Exception as e:
            print(f"Error for {country['name']}: {e}")

    # Sauvegarder les métadonnées
    with open(f'{flags_folder}/flags_metadata.json', 'w', encoding='utf-8') as f:
        json.dump(flags_data, f, indent=4)

    print(f"Download completed. {len(flags_data)} flags saved.")

if __name__ == "__main__":
    download_flags()