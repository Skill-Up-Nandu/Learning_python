# List Copying:
# Copy a list without referencing the original and modify the new one.
# any modificaion on copied list cannot affect the original one.

# create originla list
original = [1,2,3,4]

# create shallow copies of original
copied_1 = original.copy()
copied_2 = list(original)
copied_3 = original[:]

# print all lists
print('ORIGINAL :', original)
print('ORIGINAL.COPY() :', copied_1)
print('LIST(ORIGINAL) :', copied_2)
print('ORIGINAL SLICE :', copied_3)

# modify a copied list to show originals are unaffected
copied_1.append(5)
print('After modifying copied_1:', copied_1)
print('Original after modification:', original)