# Count Elements
# Given the tuple: numbers = (1, 2, 2, 3, 4, 2, 5)
# Count how many times any number appears.

numbers = (1,2,2,3,4,2,5)
print("Tuple : ",numbers)

def check_occurance():
    try :
        num = int(input("enter a number from tuple to count its occurance : "))
        if num in numbers:
            print("\nTotal Occurance : ",numbers.count(num))
        else:
            print("\nElement is not in tuple")
    except ValueError:
        print("\nInvalid Input")

check_occurance()