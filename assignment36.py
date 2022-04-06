#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: April 16, 2020



import pandas as pd

file_input = input('Enter CSV file: ')
csvFile = "file_input"
x = pd.read_csv(file_input)

y = len(x['EventID'].value_counts())
print("There were", y, "permits.")
boroughCount = x['Borough'].value_counts()
print(boroughCount)
popularLocations = x['ParkingHeld'].value_counts()[:5]
print(popularLocations)
