import matplotlib.pyplot as plt
import numpy as np
img = plt.imread('csBridge.png')
plt.imshow(img)
plt.show()
height = img.shape[0]
width = img.shape[1]
img2 = img[:height//2, width//2:]
plt.imshow(img2)
plt.show()
