# Fichier : epreuves_logiques.py
# Projet : Fort Boyard Simulator
# Auteurs : Ivan Perez
# Description : Ce fichier contient les fonctions liées à l'épreuve de bataille navale, où les joueurs
# doivent placer leurs bateaux et attaquer la grille de l'adversaire pour gagner.


import random


def grille_vide():

    """Rôle :Génère une grille vide de 3x3 pour le jeu.
      Paramètres :Aucun.
      Retourne :list : Une liste 2D de dimensions 3x3 remplie d'espaces vides (" ")."""

    return[[" " for _ in range(3)]for _ in range (3)]



def suiv(joueur):

    """Rôle :Alterne le joueur actif (0 pour le joueur humain, 1 pour le maître du jeu).
        Paramètres :joueur (int) : L'indice du joueur actuel (0 ou 1).
        Retourne :int : L'indice du joueur suivant (0 ou 1)."""

    return(joueur+1)%2



def affiche_grille(grille, message):

    """Rôle :Affiche une grille 3x3 avec un message explicatif.
      Paramètres :grille (list) : La grille à afficher (liste 2D).
                message (str) : Un message à afficher avant la grille.
      Retourne :Rien (affichage à l'écran)."""

    print(message)
    for ligne in grille:
        print(" | " + " | ".join(ligne) + " |")
    print("-" * 14)



def demande_position():

    """Rôle :Demande à l'utilisateur d'entrer une position valide sur la grille.
        Paramètres :Aucun.
        Retourne :tuple : Les coordonnées (ligne, colonne) saisies par l'utilisateur."""

    while True:
        pos = input("Entrez la position (ligne,colonne) entre 0 et 2 : ")
        if ',' in pos:
            parts = pos.split(',')
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                ligne = int(parts[0])
                colonne = int(parts[1])
                if 0 <= ligne < 3 and 0 <= colonne < 3:
                    return ligne, colonne
                else:
                    print("Position hors des limites. Réessayez.")
            else:
                print("Entrée invalide. Assurez-vous de saisir deux nombres séparés par une virgule.")
        else:
            print("Format invalide. Utilisez le format 'ligne,colonne'.")



def init():

    """Rôle :Permet au joueur de placer ses deux bateaux sur une grille 3x3.
       Paramètres :Aucun.
       Retourne :list : Une grille 3x3 avec deux bateaux positionnés."""

    grille=grille_vide()
    print("Placez vos deux bateau")
    bateau_place=0

    while bateau_place<2:
        ligne, colonne=demande_position()
        if grille[ligne][colonne]== " ":
            grille[ligne][colonne]="B"
            bateau_place +=1
        else:
            print("Place déjà occupée")
    affiche_grille(grille,"Découvrez votre grille de jeu avec vos bteau")

    return grille



def tour(joueur,grille_tir_joueur,grille_adversaire):

    """Rôle : Gère un tour de jeu où le joueur ou le maître du jeu attaque la grille adverse.
      Paramètres :
          joueur (int) : Indique le joueur actif (0 pour le joueur humain, 1 pour le maître du jeu).
          grille_tir_joueur (list) : La grille des tirs du joueur actif.
          grille_adversaire (list) : La grille contenant les bateaux de l'adversaire.
      Retourne :Rien (met à jour les grilles et affiche les résultats)."""

    if joueur==0: # Tour du joueur humain
        affiche_grille(grille_tir_joueur,"Rappel de l'historique des tirs que vous avez éffectués:")
        print("Entrez la position (ligne,colonne) entre 0 et 2 pour tirer:")
        ligne, colonne = demande_position()
    else:        # Tour du maître du jeu
        ligne, colonne= random.randint(0,2),random.randint(0,2)
        print(f"Le maître du jeu tire en position({ligne},{colonne})")

    if grille_adversaire[ligne][colonne]=="B":
        print("Touché coulé")
        grille_tir_joueur[ligne][colonne]="x"
        grille_tir_joueur[ligne][colonne]="x"
    else:
        print("Dans l'eau...")
        grille_tir_joueur[ligne][colonne] = "."




def gagne(grille_tirs_joueur):

    """Rôle :Vérifie si un joueur a coulé les deux bateaux de son adversaire.
    Paramètres :grille_tirs_joueur (list) : La grille des tirs du joueur.
    Retourne :bool : True si les deux bateaux sont coulés, False sinon."""

    return sum(row.count("x") for row in grille_tirs_joueur) == 2



def jeu_bataille_navale():
    """Rôle :Gère l'ensemble de l'épreuve de bataille navale.
       Paramètres :Aucun.
       Retourne :bool : True si le joueur humain gagne, False si le maître du jeu gagne."""


    print("Bienvenue dans le jeu de bataille navale simplifié !")
    print("Chaque joueur doit placer 2 bateaux sur une grille 3x3.")
    print("Les bateaux sont représentés par 'B' et les tirs manqués par '.'. Les bateaux coulés sont marqués par 'x'.")
    grille_joueur = init()
    grille_maitre = grille_vide()

    for _ in range(2):
        while True:
            ligne, colonne = random.randint(0, 2), random.randint(0, 2)
            if grille_maitre[ligne][colonne] == " ":
                grille_maitre[ligne][colonne] = "B"
                break

    # Initialisation des grilles
    grille_tirs_joueur = grille_vide()
    grille_tirs_maitre = grille_vide()
    joueur = 0

    while True: # Boucle principale du jeu
        if joueur == 0:
            print("C'est votre tour !")
            tour(joueur, grille_tirs_joueur, grille_maitre)
            if gagne(grille_tirs_joueur):
                print("Félicitations ! Vous avez gagné.")
                return True

        else:
            print("Tour du maître du jeu.")
            tour(joueur, grille_tirs_maitre, grille_joueur)
            if gagne(grille_tirs_maitre):
                print("Le maître du jeu a gagné.")
                return False
        joueur = suiv(joueur)