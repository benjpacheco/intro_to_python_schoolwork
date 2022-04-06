#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 9, 2020
#This program prints a list of names in a loop.

names = input("input names: ")
listOfnames = names.split(',')
for name in listOfnames:
    currentName = name.split()
    print(currentName[1][0] + '. ' + currentName[0])
