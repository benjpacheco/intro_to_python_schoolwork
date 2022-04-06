import pandas as pd
import matplotlib.pyplot as plt

pop = pd.read_csv("DHS_Daily_Report.csv")

pop['Fraction'] = pop['Total Individuals in Families with Children in Shelter'] / pop['Total Individuals in Shelter']
pop.plot(x='Date of Census', y='Fraction')

plt.show()
