#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  April 23, 2020


import pandas as pd
import matplotlib.pyplot as plt

csvIn = input("Enter your file here: ")
csvOut = input("Enter name save: ")
        
pop = pd.read_csv(csvIn)
pop['% Absent'] = pop['Absent']*100 / pop['Enrolled']
pop["Date"] = pd.to_datetime(pop["Date"].apply(str))
pop.plot(x='Date', y='% Absent')
	


plt.savefig(csvOut)
plt.show()
