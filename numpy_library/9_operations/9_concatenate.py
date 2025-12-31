# use to concate one arr into another array

import numpy as np
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])

newArray = np.concatenate((arr1 , arr2) , axis=0)
print(newArray)

newArray = np.concatenate((arr1 , arr2) , axis=1)
print(newArray)