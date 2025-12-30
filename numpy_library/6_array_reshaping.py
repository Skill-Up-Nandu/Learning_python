import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,4,5,6,8,5,2,4,6,9,5,4,8,5,6,88])
print(arr.size)
#as size is 24 : (2,12) (3,8) (4,6) (6,4) (8,3) (12,2)
new2DArray = arr.reshape(4,6)
print(arr)
print(new2DArray)

#(4,6) : (2,2,6) / (6,4) : (2,3,4) , (3,2,4) / (8,3) : (2,4,3),(4,2,3) / (12,2) : (2,6,2),(3,4,2),(4,3,2),(6,2,3)

new3DArray = arr.reshape(3,4,2)
print(new3DArray)