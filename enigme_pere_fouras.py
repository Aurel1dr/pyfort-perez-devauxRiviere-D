import json
import random


def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        return json.load(f)


def enigme_pere_fouras():
    enigmes = charger_enigmes("data/enigmesPF.json")
    enigme_choisie = random.choice(enigmes)
    question = enigme_choisie['question']
    reponse = enigme_choisie['reponse'].lower()
    essais = 3

    print("Le Père Fouras vous pose une énigme :")
    print(question)
    while essais > 0:
        tentative = input("Votre réponse : ").strip().lower()
        if tentative == reponse:
            print("Bonne réponse ! Vous avez gagné la clé.")
            return True
        essais -= 1
        if essais > 0:
            print(f"Réponse incorrecte. Il vous reste {essais} essai(s).")
        else:
            print(f"Vous avez échoué. La réponse correcte était : {reponse}.")
            return False