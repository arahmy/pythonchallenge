from turtle import *
from random import *

speed(0)
title("Quadrillage - Morpion")
Taille=600
Marge =30
setup(Taille,Taille+100)
Case=(Taille-2*Marge)//3
up()
goto(Marge-Taille//2,30-Taille//2)
down()
up()
goto(0,30-Taille//2)
down()
up()
color('black')
goto(Marge-Taille//2,Taille//2-Marge+50)
width(3)
for i in range(4):
    down()
    forward(3*Case)
    up()
    backward(3*Case)
    right(90)
    forward(Case)
    left(90)
left(90)
forward(Case)
for i in range(4):
    down()
    forward(3*Case)
    up()
    backward(3*Case)
    right(90)
    forward(Case)
    left(90)
left(90)
forward(4*Case-30)
right(90)
forward(2*Case)
mainloop()