#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 10, 2020
#This program lets tess draw a blue square, and tess a triangle.


import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("pink")


tess = turtle.Turtle()           # create tess and set some attributes
tess.color("blue")
tess.pensize(5)

alex = turtle.Turtle()           # create alex


tess.forward(80)                 # make tess draw a square
tess.left(90)
tess.forward(80)
tess.left(90)
tess.forward(80)
tess.left(90)
tess.forward(80)
tess.left(90)

tess.right(180)                  # turn tess around
tess.forward(80)                 # move her away from the origin

alex.forward(50)                 # Let alex draw an equilateral triangle
alex.left(120)
alex.forward(50)
alex.left(120)
alex.forward(50)
alex.left(120)                   # complete the triangle


wn.exitonclick()
