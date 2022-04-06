#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  April 15, 2020


file_name=input("Enter file name: ")
star_type=input("Enter the name of the star type: ") 

import numpy as np 
import pandas as pd 

data = pd.read_csv(file_name)
x=data[data['Star type'] == (star_type)]
maxValue = x['Radius(R/Ro)'].max()
minValue = x['Radius(R/Ro)'].min()

print("The radius of the largest",star_type,maxValue)
print("The radius of the smallest",star_type,minValue)
