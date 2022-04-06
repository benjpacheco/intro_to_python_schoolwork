#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 15, 2020
#This program uses the pandas lib to express a csv as a graph



import matplotlib.pyplot as plt
import pandas as pd

boroughInput = input('Enter borough: ')
boroughOutput = input('Enter output: ')
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

pop['Fraction'] = pop[boroughInput]/pop['Total']
pop.plot(x="Year", y='Fraction')

fig = plt.gcf()
fig.savefig(boroughOutput)
plt.show()
