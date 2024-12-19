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

