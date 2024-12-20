import json
import random


def salle_De_Tresor():
    with open('indicesSalles.json', 'r', encoding='utf-8') as f:
        jeu_tv = json.load(f)

    annee = random.choice(list(jeu_tv.keys()))
    emission = random.choice(jeu_tv[annee])
    indices = emission['indices']
    mot_code = emission['mot_code'].lower()
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

    if reponse_correcte:
        print("Félicitations ! Vous avez trouvé le mot-code et gagné le trésor !")
    else:
        print("Malheureusement, vous n'avez pas pu accéder au trésor.")
