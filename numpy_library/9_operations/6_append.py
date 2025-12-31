# append method append a new array at th end of existing array in regarding to x-axis(1) or y-axis(0)

import numpy as np

a =np.array([[1,2,3],[4,5,6]])

# axis not defined
demoArray = np.append(a,[7,8,9])
print(demoArray)

# along y-axis
demoArray = np.append(a , [[7,8,9]] ,axis = 0)
print(demoArray)

# along x-axis
demoArray = np.append(a , [[10],[11]], axis=1)
print(demoArray)