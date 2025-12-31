import numpy as np

#same as list indexing 
# syntax : arr[r:c]
vector  = np.array([10,50,60,80,47,5,60,50,40,50,65])
vSliced = vector[2:5]
print(f"Vector is : \n{vector}")
print(f"Sliced Vectort is : \n{vSliced}")


# syntax : arr[row range , column range] // range: start : end (end exclusive)
arr = np.arange(1,13).reshape(4,3)
print(f"\nArray is : \n{arr}")

#      0  1  2
# 0 [[ 1  2  3] 
# 1 [  4  5  6] 
# 2 [  7  8  9] 
# 3 [ 10 11 12]]


sliced = arr[1:,1]
print(f"\nSliced part is : \n{sliced}")