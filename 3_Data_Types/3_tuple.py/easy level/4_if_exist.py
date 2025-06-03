# Check if Item Exists
# Check if the value "apple" exists in the tuple: fruits = ("banana", "apple", "cherry")

fruits = ('banana', 'apple', 'cherry')
searched_fruit = input("enter the fruit for search : ")  
if searched_fruit in fruits:
    print(f"{searched_fruit} is Found !")
else:
    print(f"{searched_fruit} is Not Found !")
