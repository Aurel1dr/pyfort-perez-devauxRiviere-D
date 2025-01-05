# Fichier : epreuve_finale.py
# Projet : Fort Boyard Simulator
# Auteurs : Ivan Perez, Aurélien Devaux-Riviere
# Description : Contient la fonction pour gérer l'épreuve finale du jeu, la salle du trésor.
# Les joueurs doivent deviner un mot-code en utilisant des indices pour gagner le trésor.







import json
import random


def salle_De_Tresor():
    """
    Rôle :
        Gère l'épreuve finale de la salle du trésor. Le joueur doit deviner un mot-code en se basant
        sur des indices tirés aléatoirement d'une base de données.
    Paramètres :
        Aucun.
    Retourne :
        bool : True si le joueur trouve le mot-code, False sinon.
    """

    # Charger les données depuis le fichier JSON contenant les indices et mots-codes
    with open('data/indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)

    jeu_tv = jeu_tv["Fort Boyard"]
    annee = random.choice(list(jeu_tv.keys()))
    emission = random.choice(list(jeu_tv[annee].keys()))
    emission = jeu_tv[annee][emission]
    indices = emission['Indices']
    mot_code = emission['MOT-CODE'].lower() # Le mot-code attendu
    essais = 3 # Nombre d'essais maximum pour trouver le mot-code
    reponse_correcte = False

    # Introduction à l'épreuve
    print("\nBienvenue dans la salle du trésor !")
    print("Voici les indices pour vous aider à trouver le mot-code :")
    print(", ".join(indices[:3]))    # Afficher les trois premiers indices

    while essais > 0:# Boucle pour les tentatives du joueur
        tentative = input("Entrez votre réponse pour le mot-code : ").strip().lower()
        if tentative == mot_code:
            reponse_correcte = True
            break
        essais -= 1
        if essais > 0:
            print(f"Réponse incorrecte. Il vous reste {essais} essai(s).")
            if len(indices) > 3:      # Fournir un nouvel indice si disponible
                print(f"Nouvel indice : {indices[3]}")
                indices.pop(3) # Retirer l'indice utilisé de la liste
        else:
            print(f"Vous avez échoué. Le mot-code correct était : {mot_code}.")

    return reponse_correcte  #Résultat final retourné dans le main
