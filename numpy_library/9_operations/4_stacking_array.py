# Types of stack :
# Vertical stack : vstack : row_wise
# Horzontal Stack :hstack : column_wise
# column Stack : column_stack

# vstack only perform on vertex noton matrix

import numpy as np

A = np.array([1,2,3])
B = np.array([4,5,6])
print(f"A : {A} \nB : {B}")

vertical = np.vstack((A,B))
print(f"\nVertical Stacked : \n{vertical}")

horizontal = np.hstack((A,B))
print(f"Horizontal Stacked : \n{horizontal}")

column = np.column_stack((A,B))
print(f"Column Stacked : \n{column}")