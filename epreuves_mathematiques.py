# Fichier : epreuves_mathematiques.py
# Projet : Fort Boyard Simulator
# Auteurs : Aurélien Devaux-Riviere
# Description : Ce fichier contient les fonctions liées aux épreuves mathématiques,
# où les joueurs doivent résoudre divers problèmes pour gagner des clés.


import random


def factorielle(n):

    """Rôle :Calcule la factorielle d'un entier n.
    Paramètres :n (int) : L'entier dont on veut calculer la factorielle.
    Retourne :int : La factorielle de n."""

    factorielle = 1
    for i in range(2,n+1):
        factorielle = factorielle * i
    return factorielle



def epreuve_math_factorielle():

    """Rôle :Pose une épreuve où le joueur doit calculer la factorielle d'un nombre donné.
        Paramètres :Aucun.
        Retourne :bool : True si le joueur a donné la bonne réponse, False sinon."""

    alea = random.randint(0,10)
    print("Calculer la factorielle de",alea)
    x=int(input())
    if x == factorielle(alea) :
        print("Correct! vous avez gagné une clé")
        return True
    else :
        return False



def resoudre_equation_lineaire():

    """Rôle :Génère une équation linéaire de la forme ax + b = 0 et calcule sa solution.
       Paramètres : Aucun.
       Retourne :tuple : Contient les coefficients a, b et la solution x de l'équation."""

    a = random.randint(0, 10)
    b = random.randint(0, 10)
    x = -b/a
    return a, b ,x



def epreuve_math_equation():

    """Rôle :Pose une épreuve où le joueur doit résoudre une équation linéaire.
       Paramètres :Aucun.
       Retourne : bool : True si le joueur a donné la bonne réponse, False sinon."""

    a,b,x= resoudre_equation_lineaire()
    print("Résoudre l'équation : ", a, "x + ", b," = 0")
    valeur = float(input("Quelle est la valeur de x :"))
    if round(valeur,2)==round(x,2):
        print("Correct vous avez gagné une clé")
        return True
    else :
        print("Perdu !")
        return False



def est_premier(n):

    """Rôle :Vérifie si un nombre est premier.
     Paramètres :n (int) : Le nombre à vérifier.
     Retourne :bool : True si le nombre est premier, False sinon."""

    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % 1 == 0:
            return False
    return True



def premier_plus_proche(n):

    """Rôle :Trouve le premier nombre premier supérieur ou égal à n.
        Paramètres :n (int) : Le point de départ pour trouver un nombre premier.
        Retourne :int : Le premier nombre premier trouvé."""

    while not est_premier(n):
        n = n + 1
    return n



def epreuve_math_premier():

    """Rôle :Pose une épreuve où le joueur doit trouver le nombre premier le plus proche d'un nombre donné.
      Paramètres :Aucun.
      Retourne :bool : True si le joueur a donné la bonne réponse, False sinon."""

    n = random.randint(10, 20)
    print(f"Épreuve de Mathématiques : Trouver le nombre premier le plus proche de {n}.")
    reponse = int(input("Votre réponse : "))
    solution = premier_plus_proche(n)

    if reponse == solution:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print(f"Faux! La bonne réponse était {solution}.")
        return False




def epreuve_roulette_mathematique():

    """Rôle : Pose une épreuve où le joueur doit calculer le résultat d'une opération mathématique sur une liste de nombres générés aléatoirement.
        Paramètres :Aucun.
        Retourne :bool : True si le joueur a donné la bonne réponse, False sinon."""

    global operation_texte, resultat_correct
    nombres = []
    for _ in range(5):
        nombres.append(random.randint(1, 20))
    operation = random.choice(["addition", "soustraction", "multiplication"])

    if operation == "addition":
        resultat_correct = sum(nombres)
        operation_texte = "une addition"

    elif operation == "soustraction":
        resultat_correct = nombres[0]
        for num in nombres[1:]:
            resultat_correct -= num
        operation_texte = "une soustraction"

    elif operation == "multiplication":
        resultat_correct = 1
        for num in nombres:
            resultat_correct *= num
        operation_texte = "une multiplication"

    print(f"Nombres sur la roulette : {nombres}")
    print(f"Calculez le résultat en combinant ces nombres avec {operation_texte}.")
    reponse = int(input("Votre réponse : "))

    if reponse == resultat_correct:
        print("Bonne réponse! Vous avez gagné une clé.")
        return True
    else:
        print(f"Faux! La bonne réponse était {resultat_correct}.")
        return False




def epreuve_maths():

    """Rôle : Sélectionne aléatoirement une épreuve mathématique et l'exécute.
    Paramètres :Aucun.
    Retourne :bool : Le résultat de l'épreuve sélectionnée (True pour succès, False pour échec)."""

    epreuves = [
        epreuve_math_factorielle,
        epreuve_math_equation,
        resoudre_equation_lineaire,
        epreuve_roulette_mathematique
    ]

    epreuve = random.choice(epreuves)
    return epreuve()
