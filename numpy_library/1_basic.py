import numpy as np

# one dimensional
one = np.array([1,2,3,4])
print("ONE DIMENSIONAL ARRAY : ")
print(one)
print(f"Dimensions : {one.ndim}") #attrubute

#two dimensional
two = np.array([[1,2,3],[4,5,6]])
print("TWO DIMENSIONAL ARRAY : ")
print(two)
print(f"Dimensions : {two.ndim}")

#three dimensional 
three = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[8,5,2]]])
print("THREE DIMENSIONAL ARRAY : ")
print(three)
print(f"Dimensions : {three.ndim}")

