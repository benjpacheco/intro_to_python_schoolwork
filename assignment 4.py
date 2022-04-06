#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 11, 2020
#This program creates a loop that repeats i 150 times 
#In every iteration i changes until it reaches 150.


import turtle

tess = turtle.Turtle()

for i in range (150):
    tess.forward(0.5*i)
    tess.penup()
    tess.forward(0.5*i)
    tess.pendown()
    tess.left(110)
