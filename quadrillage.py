import turtle

# Fonction pour dessiner une ligne horizontale
def draw_horizontal_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(cell_size * 3)

# Fonction pour dessiner une ligne verticale
def draw_vertical_line(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(270)  # Orientation vers le bas
    turtle.pendown()
    turtle.forward(cell_size * 3)

# Initialisation de Turtle
turtle.speed(0)  # Vitesse maximale

# Taille de la cellule
cell_size = 100

# Dessiner le quadrillage
for i in range(1, 3):
    draw_horizontal_line(-cell_size, i * cell_size)
    draw_vertical_line(i * cell_size, -cell_size)

# Dessiner la dernière ligne verticale
draw_vertical_line(2 * cell_size, -cell_size)

# Attendre que l'utilisateur ferme la fenêtre
turtle.done()
s