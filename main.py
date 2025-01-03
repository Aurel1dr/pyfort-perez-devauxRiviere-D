from enigme_pere_fouras import *
from epreuve_finale import*
from epreuves_hasard import*
from epreuves_logiques import*
from epreuves_mathematiques import*
from fonctions_utiles import*
from data import*

def jeu():

#demander la composition de l'équipe puis joueur doit prendre décisions au fur et à mesure


#annoncer d'abord regle jeu puis création de l'équipe max 3 pers

    def jeu():

        print("Bienvenue dans le jeu de l'aventure !\n")
        print("Règles du jeu :\n")
        print("- Vous devez constituer une équipe de maximum 3 joueurs.\n")
        print("- Vous participerez à des épreuves pour gagner des clés.\n")
        print("- Une fois 3 clés obtenues, vous pourrez accéder à l'épreuve finale.\n")

        equipe = creer_equipe()
        print("\nVotre équipe est composée de :", equipe)


        cles_gagnees = 0


        while cles_gagnees < 3:
            print("\n--- Choix d'une épreuve ---")
            print("1. Épreuve de hasard")
            print("2. Épreuve logique")
            print("3. Épreuve mathématique")

            choix = input("Choisissez un type d'épreuve (1/2/3) : ")

            if choix == "1":
                joueur = selectionner_joueur(equipe)
                if epreuve_hasard(joueur):
                    cles_gagnees += 1
                    print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
                else:
                    print("Dommage, vous avez échoué cette épreuve.")

            elif choix == "2":
                joueur = selectionner_joueur(equipe)
                if epreuve_logique(joueur):
                    cles_gagnees += 1
                    print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
                else:
                    print("Dommage, vous avez échoué cette épreuve.")

            elif choix == "3":
                joueur = selectionner_joueur(equipe)
                if epreuves_mathematiques(joueur):
                    cles_gagnees += 1
                    print(f"Bravo ! Vous avez gagné une clé. Clés totales : {cles_gagnees}")
                else:
                    print("Dommage, vous avez échoué cette épreuve.")
            else:
                print("Choix invalide. Veuillez réessayer.")

        print("\nFélicitations ! Vous avez obtenu les 3 clés.")
        print("Vous accédez maintenant à l'épreuve finale.\n")

        if epreuve_finale(equipe):
            print("Bravo, vous avez remporté le trésor !")
        else:
            print("Dommage, vous avez échoué l'épreuve finale. Peut-être la prochaine fois !")


    if __name__ == "__main__":
        jeu()
