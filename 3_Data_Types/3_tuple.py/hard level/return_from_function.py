# Return Multiple Values from a Function
# Write a function that returns a tuple of the sum and product of two numbers.

# function to create a tuple
def create_tuple(a, b):
    # Return a tuple: (sum, product)
    return (a + b, a * b)

# user input
val_1 = int(input("Enter First number : "))
val_2 = int(input("Enter Second number : "))

# function call
print(f"\nValue Passes : {val_1}, {val_2}")
result = create_tuple(val_1, val_2)
print(f"My Tuple : {result}")

# unpack tuple for more understnding
sum, mul = result

print(f"\nSum of {val_1} and {val_2} : {sum}")
print(f"Product of {val_1} and {val_2} : {mul}")