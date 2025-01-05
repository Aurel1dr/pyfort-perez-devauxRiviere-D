def introduction():
    print("Bienvenue dans le jeu !")
    print("Votre objectif est d'accomplir des épreuves pour gagner des clés.")
    print("Vous devez ramasser trois clés pour accéder à la salle du trésor.")
    print("Bonne chance !\n")


def composer_equipe():
    equipe = []
    leader_designe = False

    while True:
        try:
            nombre_joueurs = int(input("Combien de joueurs souhaitez-vous inscrire dans l'équipe (1 à 3) ? "))
            if 1 <= nombre_joueurs <= 3:
                break
            else:
                print("Le nombre de joueurs doit être compris entre 1 et 3.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(nombre_joueurs):
        print(f"\nSaisissez les informations pour le joueur {i + 1} :")
        nom = input("Nom : ").strip()
        profession = input("Profession : ").strip()

        if not leader_designe:
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

    if not any(joueur["leader"] for joueur in equipe):
        print("\nAucun leader désigné. Le premier joueur sera automatiquement le leader.")
        equipe[0]["leader"] = True
    print("\nVoici la composition de l'équipe :")
    for joueur in equipe:
        role = "Leader" if joueur["leader"] else "Membre"
        print(f"- Nom : {joueur['nom']}, Profession : {joueur['profession']}, Rôle : {role}, Clés gagnées : {joueur['cles_gagnees']}")

    return equipe


def menu_epreuves():
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
    if resultat:
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

    with open("output/historique.txt", "a", encoding="utf-8") as fichier:
        fichier.write(historique_ligne)
