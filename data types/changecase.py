# program to change the cases
str = input("enter you string : ")

# all in upper case
str = str.upper()
print("UPPERCASE : ",str)

# all in lower case
str = str.lower()
print("lowercase : ",str)

# all in title case
str = str.title()
print("Title Case : ",str)

# swap the case (lower TO UPPER AND UPPER TO lower)
user_input = input("enter you string : ")
# using loop and if else
new_str1 = ""
for char in user_input:
    if char.islower():
        new_str1 += char.upper()
    elif char.isupper():
        new_str1 += char.lower()
    else:
        new_str1 += " "
print("Swap cAse : ",new_str1)

# using buit-in function
new_str2 = ""
for char in user_input:
    new_str2 += char.swapcase()
print("SWap CaSe : ",new_str2)
