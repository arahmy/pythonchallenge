import turtle
screen = turtle.Screen()
screen.title('Triangle Spiral - PythonTurtle.Academy')
turtle.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

for i in range(10,1550,9):
    turtle.fd(i)
    turtle.left(119.3)
s