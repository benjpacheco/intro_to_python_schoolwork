#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  April 3, 2020




import turtle

tess = turtle.Turtle()
myWin = turtle.Screen()     
commands = input("Please enter a command string: ")

for ch in commands:
    
    if ch == 'F':            
        tess.forward(50)
    elif ch == 'B':
        tess.backward(50)
    elif ch == 'L':         
        tess.left(90)
    elif ch == 'R':          
        tess.right(90)
    elif ch == '^':          
        tess.penup()
    elif ch == 'v':          
        tess.pendown()
    elif ch == 'r':          
        tess.color("red")
    elif ch == 'g':          
        tess.color("green")
    elif ch == 'b':          
        tess.color("blue")
    elif ch == 'p':
        tess.color("purple")
    elif ch == 'S':
        tess.stamp()
    elif ch == 'D':
        tess.dot()
            
print("See graphics window for your image")

