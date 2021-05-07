# -*- coding: utf-8 -*-

import turtle
import math

def pied(L, l):
    """Trace le pied du sapin, de longueur L et de largeur l."""
    turtle.begin_fill()
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(L)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.end_fill()
    turtle.up(); turtle.goto(L/2, l); turtle.down()
    
def long_cot(b):
    """Retourne la longueur du côté d'un triangle de base b."""
    opp = math.tan(math.pi / 6) * (b/2)
    cote = math.sqrt(opp**2 + (b/2)**2)
    return cote
    
def sapin(n, b):
    """Réalise un sapin de n étages, avec une base de b pixels."""
    if n == 1:
        turtle.begin_fill()
        turtle.forward(b/2)
        turtle.end_fill()
        # turtle.up(); turtle.forward(-b/5); turtle.down()
        boules(n)
        # turtle.up(); turtle.forward(b/5); turtle.down()
        turtle.begin_fill()
        turtle.left(150)
        turtle.forward(long_cot(b))
        turtle.left(60)
        turtle.forward(long_cot(b))
        turtle.left(150)
        turtle.end_fill()
        # turtle.up(); turtle.forward(b/5); turtle.down()
        boules(n)
        # turtle.up(); turtle.forward(-b/5); turtle.down()
        turtle.begin_fill()
        turtle.forward(b/2)
        turtle.end_fill()
        turtle.left(90)
        turtle.forward(math.tan(math.pi / 6) * (b/2))
        turtle.right(90)
    else:
        turtle.begin_fill()
        turtle.forward(b/2)
        turtle.end_fill()
        # turtle.up(); turtle.forward(-b/5); turtle.down()
        boules(n)
        # turtle.up(); turtle.forward(b/5); turtle.down()
        turtle.begin_fill()
        turtle.left(150)
        turtle.forward(long_cot(b))
        turtle.left(60)
        turtle.forward(long_cot(b))
        turtle.left(150)
        turtle.end_fill()
        # turtle.up(); turtle.forward(b/5); turtle.down()
        boules(n)
        # turtle.up(); turtle.forward(-b/5); turtle.down()
        turtle.begin_fill()
        turtle.forward(b/2)
        turtle.end_fill()
        turtle.left(90)
        turtle.forward(math.tan(math.pi / 6) * (b/2) * 0.5)
        turtle.right(90)
        sapin(n-1, b/1.2)

def etoile(x):
    """Réalise une étoile à x branches au sommet du sapin."""
    turtle.up()
    turtle.forward(-x/2) 
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.down()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(x)
        turtle.right(144)
    turtle.end_fill()
        
def boules(n):
    """Créer 2 boules de noël à chaque étages."""
    turtle.pencolor("black")
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()
    turtle.pencolor("green")
    turtle.fillcolor("green")
        
    

# turtle.speed(0)

turtle.fillcolor("brown")
pied(50, 20)
turtle.pencolor("green")
turtle.fillcolor("green")
sapin(10, 700)
turtle.pencolor("orange")
turtle.fillcolor("orange")
etoile(35)

turtle.hideturtle()
turtle.exitonclick()
turtle.clear()
