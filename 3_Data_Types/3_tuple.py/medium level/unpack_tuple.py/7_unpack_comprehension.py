# TUPLE UNPACKING IN LIST COMPREHENSION (ADVANCED)

# pairs = [(1, 2), (3, 4), (5, 6)]
# Use list comprehension to add corresponding items: [1+2, 3+4, 5+6]

pairs = [(1,2), (3,4), (5,6)]
print(f"Original List : {pairs}")

# Use unpack method
items = [a+b for (a,b) in pairs]
print(f"Unpack Method : {items}")

# Use indexing method
items = [pair[0]+pair[1] for pair in pairs]
print(f"Indexing Method : {items}")
         
