# Return Multiple Values from a Function
# Write a function that returns a tuple of the sum and product of two numbers.

# function to create a tuple
def create_tuple(a, b):
    # Return a tuple: (sum, product)
    return (a + b, a * b)

# user input
def get_data():
    try: 
        val_1 = int(input("\nEnter First number : "))
        val_2 = int(input("Enter Second number : "))
    except ValueError:
        print("Invalid Input.")
        return

    # function call
    print(f"\nValue Passes : {val_1}, {val_2}")
    result = create_tuple(val_1, val_2) 
    print(f"My Tuple : {result}")

    # unpack tuple for more understnding
    sum, prod = result
    print(f"\nSum of {val_1} and {val_2} : {sum}")
    print(f"Product of {val_1} and {val_2} : {prod}")

get_data()

