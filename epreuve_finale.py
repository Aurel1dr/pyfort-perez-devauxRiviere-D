import json
import random


def salle_De_Tresor():
    with open('data/indicesSalle.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)

    jeu_tv = jeu_tv["Fort Boyard"]
    annee = random.choice(list(jeu_tv.keys()))
    emission = random.choice(list(jeu_tv[annee].keys()))
    emission = jeu_tv[annee][emission]
    indices = emission['Indices']
    mot_code = emission['MOT-CODE'].lower()
    essais = 3
    reponse_correcte = False

    print("\nBienvenue dans la salle du trésor !")
    print("Voici les indices pour vous aider à trouver le mot-code :")
    print(", ".join(indices[:3]))

    while essais > 0:
        tentative = input("Entrez votre réponse pour le mot-code : ").strip().lower()
        if tentative == mot_code:
            reponse_correcte = True
            break
        essais -= 1
        if essais > 0:
            print(f"Réponse incorrecte. Il vous reste {essais} essai(s).")
            if len(indices) > 3:
                print(f"Nouvel indice : {indices[3]}")
                indices.pop(3)
        else:
            print(f"Vous avez échoué. Le mot-code correct était : {mot_code}.")

    return reponse_correcte
