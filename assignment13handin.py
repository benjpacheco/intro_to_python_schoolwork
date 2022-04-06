#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 18, 2020
#This program prompts an input, output, copies an image and turns it green.


import matplotlib.pyplot as plt  
import numpy as np

in_img = input("Input file: ")
out_img = input("Output file: ")
img = plt.imread(in_img)   
                       

img2 = img.copy()            
img2[:,:,0] = 0         
img2[:,:,2] = 0         

               

plt.imsave(out_img, img2)  
