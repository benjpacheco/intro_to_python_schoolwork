#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: March 13, 2020
#This program turns an image into an array and uses if statements with conditions.




import numpy as np
import matplotlib.pyplot as plt


elevations = np.loadtxt('elevationsNYC.txt')

imgBlue = float(input('Enter how blue is the ocean: '))
imgOut = input('Output file?: ')

map_shape = elevations.shape + (3,)
floodMap = np.zeros(map_shape)

for row in range(map_shape[0]):
    for col in range(map_shape[1]):
        if elevations[row,col] <= -10:
            floodMap[row,col,0] = 0.2
            floodMap[row,col,1] = 0.2
            floodMap[row,col,2] = 0.2
        elif elevations[row,col] <= 0:
            floodMap[row,col,2] = imgBlue
        elif elevations[row,col] % 10 == 0:
            floodMap[row,col,1] = 0
            floodMap[row,col,0] = 0
            floodMap[row,col,2] = 0
        else:
            floodMap[row,col,0] = 1.0
            floodMap[row,col,1] = 1.0      
            floodMap[row,col,2] = 1.0
plt.imsave(imgOut, floodMap)

               

