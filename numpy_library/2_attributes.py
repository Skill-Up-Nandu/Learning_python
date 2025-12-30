import numpy as np

one = np.array([1,2,3,4])
print(f"Array : {one}")
print(f"Shape : {one.shape}")
print(f"Size : {one.size}")
print(f"Data Type : {one.dtype}")
print(f"Dimension : {one.ndim}")

two = np.array([[1,2,3],[4,5,6]])
print(f"Array : {two}")
print(f"Shape : {two.shape}")
print(f"Size : {two.size}")
print(f"Data Type : {two.dtype}")
print(f"Dimension : {two.ndim}")

three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[8,5,2]]])
print(f"Array : {three}")
print(f"Shape : {three.shape}")
print(f"Size : {three.size}")
print(f"Data Type : {three.dtype}")
print(f"Dimension : {three.ndim}")

