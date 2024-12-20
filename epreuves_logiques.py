import random


def grille_vide():
    return [[" " for _ in range(3)] for _ in range(3)]


def suiv(joueur):
    return (joueur + 1) % 2


def affiche_grille(grille, message=""):
    if message:
        print(message)
    for ligne in grille:
        print(" | " + " | ".join(ligne) + " |")
    print("-" * 14)


def demande_position():
    while True:
        pos = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ").strip()
        if ',' in pos:
            parts = pos.split(',')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                ligne, colonne = int(parts[0]) - 1, int(parts[1]) - 1
                if 0 <= ligne < 3 and 0 <= colonne < 3:
                    return (ligne, colonne)
        print("Entrée invalide. Assurez-vous de saisir deux numéros entre 1 et 3 séparés par une virgule.")


def init():
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for bateau in range(1, 3):
        while True:
            print(f"Bateau {bateau}")
            ligne, colonne = demande_position()
            if grille[ligne][colonne] == " ":
                grille[ligne][colonne] = "B"
                break
            else:
                print("Cette case est déjà occupée. Veuillez en choisir une autre.")
    affiche_grille(grille, "Découvrez votre grille de jeu avec vos bateaux :")
    return grille


def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 0:
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués :")
        ligne, colonne = demande_position()
    else:
        ligne, colonne = random.randint(0, 2), random.randint(0, 2)
        print(f"Le maître du jeu tire en position ({ligne + 1},{colonne + 1})")

    if grille_adversaire[ligne][colonne] == "B":
        print("Touché coulé !")
        grille_tirs_joueur[ligne][colonne] = "x"
        grille_adversaire[ligne][colonne] = "x"
    elif grille_tirs_joueur[ligne][colonne] in [".", "x"]:
        print("Position déjà tirée. Vous perdez votre tour !")
    else:
        print("Dans l'eau...")
        grille_tirs_joueur[ligne][colonne] = "."


def gagne(grille_tirs_joueur):
    return sum(ligne.count("x") for ligne in grille_tirs_joueur) == 2


def jeu_bataille_navale():
    print("Bienvenue dans le jeu de bataille navale simplifié !")
    print("Chaque joueur doit placer 2 bateaux sur une grille 3x3.")
    print("Les bateaux sont représentés par 'B', les tirs manqués par '.' et les tirs réussis par 'x'.\n")

    grille_joueur = init()
    grille_maitre = grille_vide()
    for _ in range(2):
        while True:
            ligne, colonne = random.randint(0, 2), random.randint(0, 2)
            if grille_maitre[ligne][colonne] == " ":
                grille_maitre[ligne][colonne] = "B"
                break

    grille_tirs_joueur = grille_vide()
    grille_tirs_maitre = grille_vide()

    joueur = 0
    while True:
        if joueur == 0:
            print("\nC'est à votre tour de faire feu !")
            tour(joueur, grille_tirs_joueur, grille_maitre)
            if gagne(grille_tirs_joueur):
                print("Félicitations, vous avez gagné !")
                return
        else:
            print("\nC'est le tour du maître du jeu.")
            tour(joueur, grille_tirs_maitre, grille_joueur)
            if gagne(grille_tirs_maitre):
                print("Le maître du jeu a gagné !")
                return
        joueur = suiv(joueur)