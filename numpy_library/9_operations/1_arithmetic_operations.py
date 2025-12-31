# condition : Both the array should be of same size

import numpy as np

A = np.arange(1,11)
B = np.arange(11,21)
print(f"A : \n{A}\nB : \n{B}")

add = A+B
print(f"Added : \n{add}")

sub = B-A
print(f"Sub : \n{sub}")

mul = A*B
print(f"Mul : \n{mul}")

div = B/A
print(f"Div : \n{div}")

exp = B**A
print(f"Exponential : \n{exp}")


A1 = A.reshape(5,2)
print(f"\n2D Array : {A1}")

B1 = B.reshape(5,2)
print(f"\n2D Array : {B1}")

NewArray = A1 * B1
print(f"New Array : \n{NewArray}")
