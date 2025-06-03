# Tuple Unpacking
# t = (100, 200)

print("\nProgram 1 :\n")
t = (100 ,200 )
print(f"Tuple : {t}")

# unpacking the tuple
x ,y = t
print(f"First Element is : {x}")
print(f"Last Element is : {y}")

print("\n=========================================\n")

# unpack three elements
print("Program 2")
person = ("Nandini" , 24 , "Engineer")
print(f"Person : {person}\n")

# unpack into details
name , age , profession = person
print("In Detail :")
print(f"Name : {name}")
print(f"Age : {age}")
print(f"Profession : {profession}")