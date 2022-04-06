#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 18, 2020
#This program prompts a message from the user then shifts the char by 16.



txt = input("Type something: ")
word = txt
codedWord = ""
for ch in txt:
    offset = ord(ch) - ord('a') + 16 
    wrap = offset % 26  
    newChar = chr(ord('a') + wrap)  
    print(wrap, chr(ord('a') + wrap))    
    codedWord = codedWord + newChar 
    
print("Your altered word is", codedWord)
