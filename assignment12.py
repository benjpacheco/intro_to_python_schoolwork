#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 25, 2020
#This program demonstrates the shades of purple.



import turtle				

turtle.colormode(255)		
tess = turtle.Turtle()		
tess.shape("turtle")		
tess.backward(100)

for i in range(0,255,10):
     tess.forward(10)		
     tess.pensize(i)		
     tess.color(i,0,i) #sets the red and blue channels to i which makes purple over i.

