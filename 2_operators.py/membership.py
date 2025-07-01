# Membership Operators

# IN

num = [1,85,96,47,56,23,14,25,89,65,48,23]
user_num = int(input("Enter a random number  (two digit) : "))
if user_num in num:
    print("Found !")
else :
    print("Not found !")

# NOT IN 

fruits  = ("peach", "guava", "jamun", "orange", "mango", "plum", "grapes", "banana")
user_fruit = input("Ask for a fruit : ").strip().lower()
if user_fruit not in fruits:
    print("Out of stock. Come later")
else : 
    print("Your order is packed.")