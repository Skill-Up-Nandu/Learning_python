# we can aplit even numbers of rows and columns only

import numpy as np

arr = np.arange(1,13).reshape(4,3)
print(f"Array : \n{arr}" )

# rows should be of even numbers
vertical = np.vsplit(arr,2)
print(f"\nVertical Split : \n{vertical}")

# columns should be of even numbers
arr = arr.reshape(3,4)
print(f"\nArray : \n{arr}")
Horizontal = np.hsplit(arr,2)
print(f"\nHorizontal Split : \n{Horizontal}")
