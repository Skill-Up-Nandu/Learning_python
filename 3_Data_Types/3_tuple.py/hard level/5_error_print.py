# Immutable Test
# Try modifying an element in a tuple. Catch the error using try/except and print a message like "Tuples are immutable!".

numbers = (1,2,3,4,4,5,5,6,6,)

try:
    numbers[2] = 90
except TypeError:
    print("Tuple Are Immutable")

