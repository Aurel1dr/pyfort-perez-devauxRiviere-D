# Fichier : epreuves_hasard.py
# Projet : Fort Boyard Simulator
# Auteurs : Ivan Perez
# Description : Ce fichier contient les fonctions pour les épreuves de hasard,
# incluant le jeu de Bonneteau et le lancer de dés. Ces épreuves testent la chance
# des joueurs dans leur quête des clés.




import random

def bonneteau():

    """Rôle :Gère l'épreuve du Bonneteau, où le joueur doit deviner sous quel bonneteau (A, B ou C) se cache une clé.
    Paramètres :Aucun.
    Retourne :bool : True si le joueur trouve la clé, False sinon."""


    global bonneteau_cle
    bonneteaux = ['A', 'B', 'C']

    print("Bienvenue au jeu de Bonneteau !")
    print("Règles : Vous devez deviner sous quel bonneteau (A, B ou C) se cache la clé.")
    print("Vous avez 2 essais pour le trouver.")
    print("Les bonneteaux disponibles : ", ", ".join(bonneteaux))

    for tentative in range(1, 3):
        # La clé est placée aléatoirement sous un bonneteau
        bonneteau_cle = random.choice(bonneteaux)
        print(f"Tentative {tentative} : Faites votre choix parmi {', '.join(bonneteaux)}.")
        choix_joueur = input("Entrez votre choix (A, B ou C) : ").strip().upper()

        if choix_joueur in bonneteaux:
            if choix_joueur == bonneteau_cle:
                print(f"Bravo ! Vous avez trouvé la clé sous le bonneteau {choix_joueur}.")
                return True
            else:
                print(f"Dommage, la clé n'était pas sous le bonneteau {choix_joueur}. Essayez encore.")

        else:
            print("Choix invalide. Veuillez entrer A, B ou C.")
    print(f"Vous avez perdu ! La clé se trouvait sous le bonneteau {bonneteau_cle}.")

    return False




def jeu_lance_des():

    """Rôle :Gère le jeu de lancer de dés. Le joueur et le maître du jeu lancent chacun deux dés, et le premier à obtenir un 6 remporte la partie. Le jeu se déroule sur un maximum de 3 essais.
        Paramètres :Aucun.
        Retourne :bool : True si le joueur remporte la partie, False si le maître du jeu gagne ou si personne n'obtient un 6."""

    essais_max = 3
    print("Bienvenue au jeu de lancer de dés !")
    print(f"Règles : Le premier à obtenir un 6 remporte la partie. Chaque joueur a {essais_max} essais.")

    for essai in range(1, essais_max + 1):
        print(f"\n--- Essai {essai} sur {essais_max} ---")
        # Lancer des dés du joueur
        input("C'est votre tour ! Appuyez sur Entrée pour lancer les dés.")
        des_joueur = (random.randint(1, 6), random.randint(1, 6))
        print(f"Vous avez obtenu : {des_joueur[0]} et {des_joueur[1]}")

        if 6 in des_joueur:
            print("Bravo ! Vous avez obtenu un 6 et remporté la partie.")
            return True


        # Lancer des dés du maître du jeu
        print("C'est au tour du maître du jeu de lancer les dés.")
        des_maitre = (random.randint(1, 6), random.randint(1, 6))
        print(f"Le maître du jeu a obtenu : {des_maitre[0]} et {des_maitre[1]}")

        if 6 in des_maitre:
            print("Le maître du jeu a obtenu un 6 et remporte la partie.")
            return False

        print("Aucun 6 n'a été obtenu lors de cet essai. Passez au prochain round !")


    print("\nAucun joueur n'a obtenu un 6 après trois essais. C'est un match nul.")

    return False

def epreuve_hasard():

    """Rôle :Sélectionne et exécute aléatoirement une des épreuves de hasard disponibles (Bonneteau ou lancer de dés).
       Paramètres :Aucun.
       Retourne :bool : Le résultat de l'épreuve sélectionnée (True pour succès, False pour échec)."""

    epreuves = [bonneteau, jeu_lance_des]
    # Sélection aléatoire d'une épreuve
    epreuve = random.choice(epreuves)
    print("\nUne épreuve aléatoire a été sélectionnée ! Bonne chance !")
    resultat = epreuve()

    return resultat
