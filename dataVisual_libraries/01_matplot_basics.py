import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x_axis = np.linspace(5,14,15)
y_axis = x_axis ** 2

# Creating plots
plt.figure(figsize=(4,2))
plt.plot(x_axis,y_axis)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Square Function")
plt.grid(True)
plt.show()

# Creation of SUbplots

# start the figure with figsize
fig , axs = plt.subplots(2,2,figsize=(8,6))
axs[0,0].plot(x_axis,y_axis)
axs[0,0].set_title("First")
axs[0,0].set_xlabel("X -Axis")
axs[0,0].set_ylabel("Y - Axis")
axs[0,1].plot(x_axis**2,y_axis)
axs[0,1].set_title("Second")
axs[1,0].plot(y_axis,x_axis)
axs[1,0].set_title("Third")
axs[1,1].plot(x_axis,y_axis**2)
axs[1,1].set_title("Fourth")

# prevents overlays
plt.tight_layout() 

# end the figure
plt.show()