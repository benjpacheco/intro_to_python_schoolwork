#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 29, 2020
#This program turns an image into an array and uses if statements with conditions.



import numpy as np
import matplotlib.pyplot as plt


elevations = np.loadtxt('elevationsNYC.txt')

map_shape = elevations.shape + (3,)
floodMap = np.zeros(map_shape)

for row in range(map_shape[0]):
    for col in range(map_shape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = 1.0
        elif elevations[row,col] <= 6:
            floodMap[row,col,0] = 1.0
        elif 6 < elevations[row,col] <= 20:
            floodMap[row,col,1] = 0.5
            floodMap[row,col,0] = 0.5
            floodMap[row,col,2] = 0.5
        else:
            floodMap[row,col,1] = 1.0
         

plt.imsave("floodMap.png", floodMap)

