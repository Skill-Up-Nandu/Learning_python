# Return Multiple Values from a Function
# Write a function that returns a tuple of the sum and product of two numbers.

# function to create a tuple
def create_tuple(a, b):
    # Return a tuple: (sum, product)
    return (a + b, a * b)

# user input
def get_data():
    try: 
        sum_val = int(input("\nEnter First number : "))
        prod_val = int(input("Enter Second number : "))
    except ValueError:
        print("Invalid Input.")
        return

    # function call
    print(f"\nValue Passes : {sum_val}, {prod_val}")
    result = create_tuple(sum_val, prod_val) 
    print(f"My Tuple : {result}")

    # unpack tuple for more understnding
    sum, prod = result
    print(f"\nSum of {sum_val} and {prod_val} : {sum}")
    print(f"Product of {sum_val} and {prod_val} : {prod}")

get_data()

