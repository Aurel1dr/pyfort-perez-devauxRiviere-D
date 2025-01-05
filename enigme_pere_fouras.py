# Fichier : enigme_pere_fouras.py
# Projet : Fort Boyard Simulator
# Auteurs : Ivan Perez
# Description : Ce fichier contient les fonctions pour gérer l'épreuve des énigmes du Père Fouras,
# où les joueurs doivent répondre correctement à des énigmes pour gagner une clé.


import json
import random


def charger_enigmes(fichier):
    """Rôle :Charge les énigmes à partir d'un fichier JSON et les retourne sous forme de liste.
        Paramètres :fichier (str) : Le chemin du fichier JSON contenant les énigmes.
        Retourne :list : Une liste de dictionnaires, chaque dictionnaire représentant une énigme avec une question et sa réponse."""

    with open(fichier, 'r', encoding='utf-8') as f:
        return json.load(f)


def enigme_pere_fouras():
    """Rôle :Gère l'épreuve des énigmes du Père Fouras. Pose une question au joueur et vérifie sa réponse. Le joueur a trois tentatives pour répondre correctement.
        Paramètres :Aucun.
        Retourne :bool : Vrai(True) si le joueur a répondu correctement, Faux(False) sinon.
        """

    # Charger les énigmes depuis le fichier JSON
    enigmes = charger_enigmes("data/enigmesPF.json")
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie['question']
    reponse = enigme_choisie['reponse'].lower()
    essais = 3 # Nombre maximum de tentatives

    # Affichage de l'énigme au joueur
    print("Le Père Fouras vous pose une énigme :")
    print(question)

    while essais > 0: # Lecture de la réponse du joueur
        tentative = input("Votre réponse : ").strip().lower()
        if tentative == reponse:
            print("Bonne réponse ! Vous avez gagné la clé.")
            return True
        essais -= 1

        if essais > 0:
            print(f"Réponse incorrecte. Il vous reste {essais} essai(s).")
        else:             # Échec après trois tentatives
            print(f"Vous avez échoué. La réponse correcte était : {reponse}.")
            return False