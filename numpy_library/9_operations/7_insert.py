# insert is similar to append method but unlike append you can append new elementt at any position

import numpy as np

a = np.array([[1,2],[3,4],[5,6]])
print(a)

# insert without axis
demoArray = np.insert(a,3,[30,40,50])
print(f"\n{demoArray}")

# insert along x-axis(1)
demoArray = np.insert(a,1,[[50,60,70]],axis = 1)
print(f"\n{demoArray}")

# insert along y-axis(0)
demoArray = np.insert(a,0,[[88,99]], axis = 0)
print(f"\n{demoArray}")