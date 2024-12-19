import os

def introduction():
    print("=" * 50)
    print("Bienvenue dans le jeu Fort Boyard !")
    print("Règles du jeu :")
    print("1. Vous devez accomplir des épreuves pour gagner des clés.")
    print("2. L'objectif est de ramasser trois clés pour accéder à la salle du trésor.")
    print("Bonne chance à tous les participants !")
    print("=" * 50)


def composer_equipe():
    equipe = []
    while True:
        try:
            nb_joueurs = int(input("Combien de joueurs voulez-vous inscrire dans l'équipe ? (max 3) : "))
            if 1 <= nb_joueurs <= 3:
                break
            print("Erreur : L'équipe doit comprendre entre 1 et 3 joueurs.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(nb_joueurs):
        print(f"\nInscription du joueur {i + 1} :")
        nom = input("Nom : ").strip()
        profession = input("Profession : ").strip()
        est_leader = input("Est-ce le leader de l'équipe ? (oui/non) : ").strip().lower() == 'oui'
        joueur = {
            "nom": nom,
            "profession": profession,
            "leader": est_leader,
            "cles_gagnees": 0
        }
        equipe.append(joueur)

    if not any(joueur["leader"] for joueur in equipe):
        print("Aucun leader désigné. Le premier joueur devient automatiquement le leader.")
        equipe[0]["leader"] = True

    return equipe

