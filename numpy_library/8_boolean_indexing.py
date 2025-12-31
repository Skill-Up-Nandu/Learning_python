# Used for filtering elements from an array based on a specific condition , employeing a boolean mask

import numpy as np

arr = np.arange(1,21)
print(f"Array is : \n{arr}")

# we want only odd numbers in arr

bool_indexing = arr % 2 != 0
print(f"Bool indexing Array : \n{bool_indexing}")

arr = arr[bool_indexing]
print(f"Array with Odd numbers only : \n{arr}")