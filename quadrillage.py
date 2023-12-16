from turtle import *
from colorama import *

def Quadrillage(x, y, taille, nb):
    up()
    goto(x - taille / 2, y - taille / 2)
    down()
    up()
    goto(x, y - taille / 2)
    down()
    up()
    color('black')
    width(3)
    for i in range(nb + 1):
        down()
        forward(nb * taille)
        up()
        backward(nb * taille)
        right(90)
        forward(taille)
        left(90)
    left(90)
    forward(taille)
    for i in range(nb + 1):
        down()
        forward(nb * taille)
        up()
        backward(nb * taille)
        right(90)
        forward(taille)
        left(90)
    left(90)
    forward((nb + 1) * taille)
    right(90)
    forward((nb - 1) * taille / 2)

# Input - Prise en compte des paramètres
x = float(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la coordonnée x : "))
y = float(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la coordonnée y : "))
taille = float(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la taille de chaque case" + Fore.YELLOW + " (La taille 10 est recommandée) : " + Fore.RESET))
nb_cases = int(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez le nombre de cases par côté : "))

speed(0)
title("Quadrillage - Morpion")
setup(800, 800)

# Appel fonction
Quadrillage(x, y, taille, nb_cases)

# Laisser la page ouverte
mainloop()
