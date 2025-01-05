# Fichier : fonctions_utiles.py
# Projet : Fort Boyard Simulator
# Auteurs : Ivan Perez, Aurélien Devaux-Riviere
# Description : Ce fichier regroupe des fonctions utilitaires pour gérer les étapes du jeu,
# comme l'introduction, la composition de l'équipe, le choix des épreuves, la sélection
# des joueurs et l'enregistrement de l'historique.



def introduction():

    """Rôle :Affiche un message d'introduction pour expliquer les règles générales du jeu.
       Paramètres :Aucun.
       Retourne :Rien (simple affichage)."""

    print("Bienvenue dans le jeu !")
    print("Votre objectif est d'accomplir des épreuves pour gagner des clés.")
    print("Vous devez ramasser trois clés pour accéder à la salle du trésor.")
    print("Bonne chance !\n")


def composer_equipe():

    """Rôle :Permet à l'utilisateur de créer une équipe de joueurs (1 à 3 membres), en collectant leur nom, profession, et en désignant un leader.
        Paramètres :Aucun.
        Retourne :list : Une liste de dictionnaires, chaque dictionnaire représentant un joueur avec les clés 'nom', 'profession', 'leader' et 'cles_gagnees'."""

    equipe = []
    leader_designe = False

    while True: # Saisie du nombre de joueurs
        try:
            nombre_joueurs = int(input("Combien de joueurs souhaitez-vous inscrire dans l'équipe (1 à 3) ? "))
            if 1 <= nombre_joueurs <= 3:
                break
            else:
                print("Le nombre de joueurs doit être compris entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(nombre_joueurs):# Saisie des informations pour chaque joueur
        print(f"\nSaisissez les informations pour le joueur {i + 1} :")
        nom = input("Nom : ").strip()
        profession = input("Profession : ").strip()

        if not leader_designe:# Désignation du leader
            leader = input("Ce joueur est-il le leader de l'équipe ? (oui/non) : ").strip().lower()
            if leader == "oui":
                leader_designe = True
                est_leader = True
            else:
                est_leader = False

        else:
            print("Un leader a déjà été désigné. Ce joueur ne peut pas être le leader.")
            est_leader = False

        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": est_leader,
            "cles_gagnees": 0
        }
        equipe.append(joueur)

    if not any(joueur["leader"] for joueur in equipe):    # Si aucun leader n'est désigné, le premier joueur devient leader automatiquement après la présentation de chaque joueur
        print("\nAucun leader désigné. Le premier joueur sera automatiquement le leader.")
        equipe[0]["leader"] = True

    print("\nVoici la composition de l'équipe :")            # Affichage de la composition de l'équipe
    for joueur in equipe:
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"- Nom : {joueur['nom']}, Profession : {joueur['profession']}, Rôle : {role}, Clés gagnées : {joueur['cles_gagnees']}")

    return equipe


def menu_epreuves():

    """Rôle :Affiche un menu pour permettre à l'utilisateur de choisir un type d'épreuve.
        Paramètres :Aucun.
        Retourne :int : Le numéro correspondant au choix de l'épreuve (entre 1 et 4)."""

    print("\nMenu des épreuves :")
    print("1. Épreuve de Mathématiques")
    print("2. Épreuve de Logique")
    print("3. Épreuve du Hasard")
    print("4. Énigme du Père Fouras")

    while True:
        try:
            choix = int(input("Choix : "))
            if 1 <= choix <= 4:
                return choix
            else:
                print("Veuillez entrer un numéro entre 1 et 4.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


def choisir_joueur(equipe):

    """Rôle :Permet de sélectionner un joueur dans l'équipe pour participer à une épreuve.
      Paramètres :equipe (list) : Liste des joueurs de l'équipe.
      Retourne :dict : Le dictionnaire représentant le joueur sélectionné."""

    print("\nChoisissez un joueur pour cette épreuve :")
    index = 1
    for joueur in equipe:
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"{index}. {joueur['nom']} ({joueur['profession']}) - {role}")
        index += 1

    while True:
        try:
            choix = int(input("Entrez le numéro du joueur : "))
            if 1 <= choix <= len(equipe):
                return equipe[choix - 1]
            else:
                print(f"Veuillez entrer un numéro entre 1 et {len(equipe)}.")
        except ValueError:
            print("Veuillez entrer un numéro valide.")


def enregistrer_historique(nom_joueur, epreuve, resultat, cles_gagnees):

    """Rôle :Enregistre les résultats d'une épreuve dans un fichier texte.
        Paramètres :nom_joueur (str) : Le nom du joueur ayant participé. epreuve (str) : Le type d'épreuve (ex. : 'Mathématiques'). resultat (str) : Le résultat de l'épreuve ('Réussi' ou 'Échoué'). cles_gagnees (int) : Le nombre total de clés obtenues après cette épreuve.
        Retourne :Rien (sauvegarde dans un fichier texte)."""

    if resultat: # Formater les données à enregistrer
        sortie = "Gagné"
    else :
        sortie = "Perdu"
    historique_ligne = (
        f"Joueur : {nom_joueur}\n"
        f"Épreuve : {epreuve}\n"
        f"Résultat : {sortie}\n"
        f"Clés gagnées : {cles_gagnees}\n"
        f"{'-' * 40}\n"
    )

    with open("output/historique.txt", "a", encoding="utf-8") as fichier:     # Sauvegarder dans le fichier historique
        fichier.write(historique_ligne)
