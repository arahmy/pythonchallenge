"""
# Défi 1 - Exercice a
import turtle
from turtle import *
screen = turtle.Screen()
screen.title('Carré en Spirale - Défi 1')

long=400
up()
speed(0)
left(90)
goto(225,-255)
down()
while long > 20:
    long = long - (long*2/100)
    forward(long)
    left(93)
"""

# Défi 1 - Exercice b
"""
import turtle

screen = turtle.Screen()
screen.title('Triangle en Spirale - Défi 1')
turtle.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

for i in range(10,1550,9):
    turtle.fd(i)
    turtle.left(119.3)

turtle.mainloop() # Laisser la page ouverte
"""
"""
# Défi 2
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
# Float = Permet de convertir un nombre entier en un à nombre à virgule
print(Fore.BLUE + "[Défi Python - Logs]" + Fore.RESET + " Vous avez lancé le programme.")
x = float(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la coordonnée x : "))
y = float(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la coordonnée y : "))
taille = float(input(
    Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez la taille de chaque case" + Fore.YELLOW + " (La taille 10 est recommandée) : " + Fore.RESET))
nb_cases = int(input(Fore.RED + "[Défi Python]" + Fore.RESET + " Entrez le nombre de cases par côté : "))

speed(0)
title("Quadrillage - Morpion")
setup(800, 800)

# Appel fonction
Quadrillage(x, y, taille, nb_cases)

# Laisser la page ouverte

turtle.Screen().exitonclick()
print(Fore.BLUE + "[Défi Python - Logs]" + Fore.RESET + " Vous avez mis fin au programme.")
"""
"""
# Défi 3 - Dictionnaire :
def stat(txt):
    dic = {}
    # Parcourir chaque caractère dans le texte
    for char in txt:
        # Ignorer les espaces
        if char != ' ':
            # Utiliser get() pour obtenir la valeur
            dic[char] = dic.get(char, 0) + 1

    return dic

# Appel Fonction + Print
resultat = stat("TAGADA BONBONS ")
print(resultat)
"""
# Défi 4 - Forêt

import turtle
from turtle import *
import random
from colorama import *

def drawtree(x, y, taille):
    speed(10) # Vitesse accélérée
    # Modèle de base du sapin
    color("saddlebrown")
    begin_fill()
    penup()
    goto(x - taille / 10, y - taille / 5)  # Permet de centrer le tronc du sapin en le commençant vers la gauche pour plus d'équilibre
    pendown()
    for _ in range(2):
        forward(taille / 5)
        right(90)
        forward(taille / 10)
        right(90)
    end_fill()

# Permet de faire des réglagles sur la couleur, la position initiale, dessiner les branches, et le remplissage (couleur=

    color("forestgreen")
    penup()
    goto(x - taille / 2, y - taille / 5)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(taille)
        left(120)
    end_fill()

    penup()
    goto(x - taille / 2 + 10, y + taille / 5)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(taille - 20)
        left(120)
    end_fill()

    penup()
    goto(x - taille / 2 + 20, y + taille / 2)
    pendown()
    begin_fill()
    for _ in range(3):
        forward(taille - 40)
        left(120)
    end_fill()

# Informations Screen - Paramètres
screen = turtle.Screen()
screen.title('Sapin de Noel - Défi Python')

# Génération aléatoire entre 1 et 50 sapins + Message d'information
gen_sapins = random.randint(1, 50)
print(Fore.RED + "[Défi Python - Info] " + Fore.RESET + "Le nombre de sapin choisi est", gen_sapins)

# Génération aléatoire des tailles et des positions
for _ in range(gen_sapins):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    taille = random.randint(50, 150)
    drawtree(x, y, taille)

done()