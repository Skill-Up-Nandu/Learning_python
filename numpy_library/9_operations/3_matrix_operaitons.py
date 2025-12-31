import numpy as np

# dot product (multipy between two matrix)
# condition  row_size of arr1 == column_size of arr2 and vice versa

arr1 = np.array([[1,2],
                [3,4],
                [5,6]])
arr2 = np.array([[7,8,9],
                [10,11,12]])

mul = arr1 @ arr2
print(mul)

dot = np.dot(arr1,arr2)
print(f"\n{dot}")


# transpose create new array with interchanging row into column and column into row

transpose_arr1 = arr1.T
print(transpose_arr1)
