# how to reverse a string
str = input("enter an idiom : " )
print("Original String")
print(str)
str_one = str[::-1]
print("Reverse By character : ")
print(str_one)   # whole words qith character
print("Reverse by words : ")
str_two = str.split()
str_two = str_two[::-1]
print(" ".join(str_two))
