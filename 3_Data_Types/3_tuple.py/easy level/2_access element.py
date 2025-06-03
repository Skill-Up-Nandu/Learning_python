# Access Elements
# Given the tuple t = (10, 20, 30, 40, 50), print the third element.

t = (10,20,30,40,50)

# beginner level accessing third element 
print(f"Thisr Element is : {t[2]}")

# medium level accessing element
try:
    mid_index = int(input("Enter item number to access : "))
    if 1 <= mid_index <= len(t):
        print(f"The {mid_index} element is : {t[mid_index-1]}")
    else:
        print("\nNumber is out of range. Try again")
except ValueError :
    print("Invalid Input.")

