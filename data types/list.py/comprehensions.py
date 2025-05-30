# List Comprehension:
# Create a list of squares from 1 to 10 using list comprehension.

squares = []

# creating list of squares using traditional loop
for x in range(1,11):
    squares.append(x**2)
print(squares)

# creating list of squares using comprehensions
square = [x**2 for x in range(1,11)]
print(square)