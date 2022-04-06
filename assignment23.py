#Name:  Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date:  Mar 3, 2020
#This program loads an image, counts the number of pixels that are white


import matplotlib.pyplot as plt
import numpy as np

img_input = input('Enter a png: ')
ca = plt.imread(img_input)   
countSnow = 0           
t = 0.75
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)
