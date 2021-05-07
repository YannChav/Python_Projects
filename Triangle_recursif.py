# -*- coding: utf-8 -*-

import turtle

#Exercice 1:

def koch(L,n):
  if n == 0:
    return turtle.forward(L)
  else:
    koch(L/3,n-1)
    turtle.left(60)
    koch(L/3,n-1)
    turtle.right(120)
    koch(L/3,n-1)
    turtle.left(60)
    return koch(L/3,n-1)

#Exercice 2:
    
def triangle(L,n):
    if n == 0:
        turtle.begin_fill()
        turtle.forward(L)
        turtle.left(120)
        turtle.forward(L)
        turtle.left(120)
        turtle.forward(L)
        turtle.left(120)
        turtle.end_fill()
    else:
        turtle.begin_fill()
        triangle(L/2,n-1)
        turtle.forward(L)
        turtle.left(120)
        triangle(L/2,n-1)
        turtle.forward(L)
        turtle.left(120)
        triangle(L/2,n-1)
        turtle.forward(L)
        turtle.left(120)
        turtle.end_fill()
        

turtle.speed(0)
x = 450
# turtle.fillcolor("green")
# triangle(x,0)
turtle.fillcolor("red")
triangle(x,5)

turtle.hideturtle()
turtle.exitonclick()
turtle.clear()
        
         
        
        