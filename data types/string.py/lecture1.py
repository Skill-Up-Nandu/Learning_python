print("\n In Python, a string is just a snobby list of characters with quotation marks!")
print("Lets undersand the string data type in Python")
str = input("share your thought ! : ")
print("The string is: ", str)
#accessing any cahracters in string
print("Total letters : ",len(str))
i = int(input("which character ? : "))
print(str[i],"(indexing strarts from 0)")

#concatenate
init = "I think , you are "
comment = "...../ complete the sentence"
print(init + comment)
end = input()
print(init+end)

# slicing
print("Traversing")
print(str[::])
print("OPPOSITE :")
newStr = str.split() # converts into list elements
print(" ".join(newStr[::-1]))
change case
case = input("write a sentence in mix case : ")
change = ""
for el in case:
    if el.islower():
        change += el.swapcase()
    elif el.isupper():
        change += el.swapcase()
    else:
        change += " "
print(change)