# Fichier : main.py
# Projet : Fort Boyard Simulator
# Auteurs : [Vos noms ici]
# Description : Point d'entrée principal du jeu. Ce fichier coordonne les différentes épreuves
# et gère le déroulement global, de la création de l'équipe à l'épreuve finale.



from enigme_pere_fouras import*
from epreuve_finale import*
from epreuves_hasard import*
from epreuves_logiques import*
from epreuves_mathematiques import*
from fonctions_utiles import*



def jeu():

    """Rôle :Gère le déroulement complet du jeu, enchaînant les étapes depuis l'introduction, la création de l'équipe, les épreuves, jusqu'à l'épreuve finale.
        Paramètres : Aucun.
        Retourne : Rien (affiche les messages du déroulement du jeu et les résultats)."""

    print("Bienvenue dans ce jeu inspiré de Fort Boyard!\n")
    print("Règles du jeu :\n")
    print("- Vous devez constituer une équipe de maximum 3 joueurs.\n")
    print("- Vous participerez à des épreuves pour gagner des clés.\n")
    print("- Une fois 3 clés obtenues, vous pourrez accéder à l'épreuve finale.\n")
    equipe = composer_equipe()  # Création de l'équipe de joueurs
    cles_gagnees = 0

    while cles_gagnees < 3:# Boucle principale pour gagner les 3 clés
        print("\n--- Choix d'une épreuve ---")
        print("1. Épreuve de hasard")
        print("2. Épreuve logique")
        print("3. Épreuve mathématique")
        print("4. Enigme du Pere Fouras")
        choix = input("Choisissez un type d'épreuve (1/2/3/4) : ")

        if choix == "1":
            joueur = choisir_joueur(equipe)
            resultat = epreuve_hasard()             # éxécution de l'épreuve de hasard
            if resultat:
                cles_gagnees += 1
                print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
            else:
                print("Dommage, vous avez échoué cette épreuve.")
            enregistrer_historique(joueur['nom'], "epreuve_hasard", resultat, cles_gagnees)

        elif choix == "2":                    # éxécution de l'épreuve logique (Bataille navale)
            joueur = choisir_joueur(equipe)
            resultat = jeu_bataille_navale()
            if resultat:
                cles_gagnees += 1
                print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
            else:
                print("Dommage, vous avez échoué cette épreuve.")
            enregistrer_historique(joueur['nom'], "jeu_bataille_navale", resultat, cles_gagnees)

        elif choix == "3":                   # éxécution de l'épreuve mathématique
            joueur = choisir_joueur(equipe)
            resultat = epreuve_maths()
            if resultat:
                cles_gagnees += 1
                print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
            else:
                print("Dommage, vous avez échoué cette épreuve.")
            enregistrer_historique(joueur['nom'], "epreuve_maths", resultat, cles_gagnees)

        elif choix== "4": # éxécution de l'énigme du Père Fouras
            joueur = choisir_joueur(equipe)
            resultat = enigme_pere_fouras()
            if resultat:
                cles_gagnees += 1
                print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
            else:
                print("Dommage, vous avez échoué cette épreuve.")
            enregistrer_historique(joueur['nom'], "enigme_pere_fouras", resultat, cles_gagnees)
        else:
            print("Choix invalide. Veuillez réessayer.")

    # Accès à l'épreuve finale une fois les 3 clés obtenues
    print("\nFélicitations ! Vous avez obtenu les 3 clés.")
    print("Vous accédez maintenant à l'épreuve finale.\n")

    resultat = salle_De_Tresor()
    if resultat:
        print("Bravo, vous avez remporté le trésor !")
    else:
        print("Dommage, vous avez échoué l'épreuve finale. Peut-être la prochaine fois !")
    enregistrer_historique(joueur['nom'], "salle_De_Tresor", resultat, cles_gagnees)


if __name__ == "__main__":

    """Point d'entrée du programme. Exécute la fonction jeu() pour démarrer le jeu."""

    jeu()
