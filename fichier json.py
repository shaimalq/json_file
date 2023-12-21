import json

# 1. Création d'un fichier JSON nommé "data.json"
data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

# Écriture du dictionnaire dans un fichier
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# 2. Lecture du fichier "data.json" et affichage de son contenu sous forme de dictionnaire
with open('data.json', 'r') as f:
    data_loaded = json.load(f)
    print(data_loaded)

# 3. Ajout d'une nouvelle clé-valeur "langage": "Python" au dictionnaire
data_loaded['langage'] = 'Python'

# 4. Enregistrement du dictionnaire modifié dans le fichier "data.json"
with open('data.json', 'w') as f:
    json.dump(data_loaded, f, indent=4)

# 5. Affichage du contenu du fichier "data.json" après la modification
with open('data.json', 'r') as f:
    data_updated = json.load(f)
    print(data_updated)