# TUPLE UNPACKING IN LIST COMPREHENSION (ADVANCED)

# Given:
# pairs = [(2, 3), (4, 5), (6, 7)]

# Create a list of the product of each pair.
# Expected Output: [6, 20, 42]

pairs = [(2, 3), (4, 5), (6, 7)]
print(f"Original List : {pairs}")

# unpacking using comprehension
mul = [a*b for (a,b) in pairs]
print(f"Multiply List : {mul}")