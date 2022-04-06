#Name: Benyir J Pacheco
#Email: benyir.pacheco60@myhunter.cuny.edu.
#Date: February 18, 2020
#This program prints a U logo on a 30x30 array.


import matplotlib.pyplot as plt  
import numpy as np

logoimg = np.ones((30,30,3))
logoimg[:,:10,1] = 0
logoimg[:,:10,2] = 0
logoimg[:,-10:,1] = 0
logoimg[:,-10:,2] = 0
logoimg[20:30,:,1] = 0
logoimg[20:30,:,2] = 0

plt.imshow(logoimg)		
plt.show()

plt.imsave('logo.png', logoimg)
