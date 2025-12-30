import numpy as np

#array creation using range
ranged_arr = np.arange(3,8)  # end indx is exclusive
print(ranged_arr)

ranged_gap_arr = np.arange(3,8,2)  # (strt , end , step(default = 0))
print(ranged_gap_arr)

# zero matrices
zeroVertex = np.zeros(5)
print(zeroVertex)

zeroVertices = np.zeros((3,4))
print(zeroVertices)

# ones matrices
onesVertex = np.ones(5)
print(onesVertex)

onesVertices = np.ones((3,4))
print(onesVertices)


#linear space array

linearArray = np.linspace(1,5,2)
#(start_range , end_range , total_elements from given range )
print(linearArray)
linearArray = np.linspace(1,5,3)
print(linearArray)
linearArray = np.linspace(1,2,3)
print(linearArray)