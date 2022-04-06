#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 4, 2020
#This program converts an input into an integer then prints its remaining cents



cents = int(input("Enter the number of cents here: "))

quarters = cents // 25

print("Quarters:", quarters)

rem = cents % 25

dimes = rem // 10

print("Dimes:", dimes)

rem = rem % 10

nickles = rem // 5

print("Nickles:", nickles)

cents = rem % 5

print("Cents:", cents)
