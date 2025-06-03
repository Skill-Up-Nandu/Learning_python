# Slice a Tuple
# From the tuple t = (10, 20, 30, 40, 50, 60), print a new tuple that contains the middle 3 elements.

t = (10,20,30,40,50,60)
print("Original Tupl : ",t)
idx = len(t) // 2
print("Sliced Tuple : ",t[idx-1 :idx+2])