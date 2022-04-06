import numpy as np
import matplotlib.pyplot as plt
im = np.ones( (10,10,3) )
im[1::2, 1::2, :]  = 0
plt.matshow(im)
plt.show()
