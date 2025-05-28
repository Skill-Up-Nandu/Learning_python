# count the vowels appears in a sting
str = input("enter your father's name : ")
count = 0
print("total letter : ",len(str))
# using for loop
for i in str:
    if i=="a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1
    else:
        count += 0
print("There are",count,"vowels and",len(str)-count,"consonets in",str)

# using while loop
count_vow = 0
i = 0
while i < len(str):
    if str[i]=="a" or str[i] == "e" or str[i] == "i" or str[i] == "o" or str[i] == "u":
        count_vow += 1
    else:
        count_vow += 0
    i += 1
print("There are",count,"vowels  and",len(str)-count,"consonets in",str)

