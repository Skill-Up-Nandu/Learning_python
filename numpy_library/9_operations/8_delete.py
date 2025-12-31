# it is use to delete elements from existing array

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

# delete without axis
demoArray = np.delete(a,5)
print(f"\n{demoArray}")

# delete along x-axis(1)
demoArray = np.delete(a,2,axis=0)
print(f"\n{demoArray}")

# delete along y-axis(0)
demoArray = np.delete(a,1,axis=1)
print(f"\n{demoArray}")