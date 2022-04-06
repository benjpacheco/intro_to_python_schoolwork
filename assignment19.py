import numpy as np
import matplotlib.pyplot as plt

num = int(input("Input size: "))
out_img = input("Output file: ")
   
img = np.ones( (num,num,3) )

img[::,0:num:1,0:2] = 0

plt.imshow(img)
plt.show()
plt.imsave(out_img, img)
