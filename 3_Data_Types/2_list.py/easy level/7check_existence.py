# Check Existence:
# Check if "apple" is present in the list fruits.

bucket = ["mango", "kiwi", "raspberry","guava","watermelon"]

# function to check whether the fruit is present or not
def check_existence(fruit):
    if fruit in bucket:
        print(fruit,"is Present in ",bucket)
    else:
        print(fruit," is Not Present in",bucket)

# function calls to check for particular fruits
check_existence('kiwi')
check_existence('mango')
check_existence('apple')
