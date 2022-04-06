import matplotlib.pyplot as plt
import numpy as np

logoimg = np.ones((30,30,3))
logoimg[::2,:,1] = 0
logoimg[::2,:,2] = 0

plt.imshow(logoimg)
plt.show()

plt.imsave('logo.png', logoimg)
