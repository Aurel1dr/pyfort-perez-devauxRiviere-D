import random


def factoriel(n):
    factoriel = 1
    for i in range(2,n+1):
        factoriel = factoriel * i
    return factoriel






def epreuve_math_factorielle():
    alea = random.randint(0,10)
    print("Calculer la factorielle de",alea)
    x=int(input())
    if x == factoriel(alea) :
        print("Correct! vous avez gagné une clé")
        return True
    else :
        return False

print(epreuve_math_factorielle())






def resoudre_equation_lineaire():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    x = -b/a
    return a, b ,x







def epreuve_math_equation():
    a,b,x= resoudre_equation_lineaire()
    print("Résoudre l'équation : ", a, "x + ", b," = 0")
    valeur = float(input("Quelle est la valeur de x :"))
    if round(valeur,2)==round(x,2):
        print("Correct vous avez gagné une clé")
        return True
    else :
        print("Perdu ! Looserrrrrr")
        return False

print(epreuve_math_equation())






def est_premier(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % 1 == 0:
            return False
    return True






def premier_plus_proche(n):
    while not est_premier(n):
        n = n + 1
    return n







def epreuve_math_premier():
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







def epreuve_math_premier():
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
            resultat_correct = resultat_correct - num
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
