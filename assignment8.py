#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 18, 2020
#This program prompts a message from the user then prints it backwards.




txt = input("Type something: ")
for x in range(len(txt)-1 , -1, -1):

     print(txt[x], end='')
