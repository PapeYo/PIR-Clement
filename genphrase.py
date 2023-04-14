import json
import random

# Charger le fichier JSON
with open('genphrase.json') as f:
    data = json.load(f)

# Accéder aux sections
sujets = data['sujet']
actions = data['action']
localisations = data['localisation']

# Sélectionner un élément aléatoire de chaque section
sujet = random.choice(sujets)
action = random.choice(actions)
localisation = random.choice(localisations)

# Générer la phrase
phrase = localisation + ' : ' + sujet + ' ' + action

# Afficher la phrase
print(phrase)