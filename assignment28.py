#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 15, 2020
#This program uses the pandas lib to express series functions





import matplotlib.pyplot as plt
import pandas as pd

boroughInput = input('Enter borough: ')
pop = pd.read_csv('nycHistPop.csv',skiprows=5)


print("Min pop: ", pop[boroughInput].min())
print("Max pop: ", pop[boroughInput].max())
print("Avg pop: ", pop[boroughInput].mean())
print("Standard dev: ", pop[boroughInput].std())
