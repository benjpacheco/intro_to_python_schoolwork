#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  May 4, 2020


acc = 0
total = 0
count = 0
while acc < 50:
    num = float(input('Please enter a number: '))
    total = total + num
    count = count + 1
    acc = total/count
    
    print('Your avg is:',acc)
