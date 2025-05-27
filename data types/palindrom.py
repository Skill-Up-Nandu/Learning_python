# check weather the string is palindrom or not
str = input("Enter your name : ")
if str == str[::-1]:
    print(str," is a plindrom.")
else:
    print(str," is not palindrom.")