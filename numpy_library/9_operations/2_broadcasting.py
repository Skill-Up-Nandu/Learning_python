# As similar to arithmetic operation but here we braodcast all elements of one array using arithmetic operators

import numpy as np
arr = np.arange(10,21)

print(f"Array : {arr}")

arr = arr ** 2

print(f"Broadcast Array : {arr}")


# another example

marks = np.array([450,856,954,365,745,922,487,555])

percentage = marks / 1000 * 100

print(f"Percentage of all students")
for idx , per in enumerate(percentage,1) :
    print(f"{idx}. {per.round(2)}%")

#we can also bradcast matrx in similar way 