import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Array : {arr}")

print(f"Max Element : {arr.max()}")
print(f"Index of Max Element : {arr.argmax()}")
print(f"Min Element : {arr.min()}")
print(f"Index of Min Element : {arr.argmin()}")
print(f"Mean of all Elements : {arr.mean()}")
print(f"Standard Deviation of all Elements : {arr.std()}")

#sum of elements

print(f"Sum of all elements : {arr.sum()}")

#row_wise  x - axis = 1
print(f"Sum of all rows : {np.sum(arr , 1)}")

#column_wise y - axis = 0
print(f"Sum of all columns : {np.sum(arr , 0)}")
