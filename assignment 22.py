#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 10, 2020
#This program creates a loop of an int input



import turtle

turns = int(input('Enter number of turns: '))
ben = turtle.Turtle()


for i in range(0,turns,2):
    ben.forward(i)
    ben.right(45)
