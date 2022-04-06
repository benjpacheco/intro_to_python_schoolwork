


import matplotlib.pyplot as plt  
import numpy as np

in_img = input("Input file: ")
out_img = input("Output file: ")
img = plt.imread(in_img)   
plt.imshow(img)		
plt.show()                         

img2 = img.copy()            
img2[:,:,0] = 0         
img2[:,:,2] = 0         

plt.imshow(img2)         
plt.show()               

plt.imsave(out_img, img2)  
