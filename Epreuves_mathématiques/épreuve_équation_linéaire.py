import random

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