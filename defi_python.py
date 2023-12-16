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

Def Quadrillage(x,y,taille,nb):
setup(1300,1000)
speed(1)
goto(x,y)
down()
"""


"""
setup(1300,1000)
speed(5)
down()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(50)
left(180)
forward(100)
right(90)
forward(50)
left(180)
forward(100)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(180)
forward(100)
left(90)
forward(50)
"""

mainloop()