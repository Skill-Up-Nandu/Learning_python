import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('image.jpg')
print(img)
plt.imshow(img)
plt.axis('off')
plt.show()