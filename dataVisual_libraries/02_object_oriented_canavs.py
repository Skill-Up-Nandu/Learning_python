import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_axis = np.linspace(5,14,15)
y_axis = x_axis ** 2

fig = plt.figure()
axis1 = fig.add_axes([0.1,0.1,0.8,0.8])
axis1.plot(x_axis,y_axis)
axis2 = fig.add_axes([0.3,0.25,0.4,0.4])
axis2 = plt.plot(y_axis,x_axis)
plt.show()