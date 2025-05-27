# program to find duplicate characters
input_str = input("Enter any string :")
duplicate = ""
for char in set(input_str):
    if input_str.count(char) > 1:
        duplicate += char
print("Duplicate characters are : ", duplicate)