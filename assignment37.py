#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: April 17, 2020



x = input("Enter a string: ")
upper = 0
lower = 0
num = 0
spec = 0


for ch in x:
    char = ord(ch)
    if 65 <= char < 91:
        upper = upper + 1
    elif 97 <= char < 123:
        lower = lower + 1
    elif 48 <= char < 58:
        num = num + 1
    else :
        spec = spec + 1

print("Your codeword contains "+str(upper)+" uppercase letters, "+str(lower)+" lowercase letters, "+str(num)+" numbers, and "+str(spec)+" special characters.")
