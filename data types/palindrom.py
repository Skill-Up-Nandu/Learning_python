# check weather the string is palindrom or not
# A palindrome is a word, phrase, number, or sequence that reads the same backward as forward.

str = input("Enter your name : ")
if str == str[::-1]:
    print(str," is a plindrom.")
else:
    print(str," is not palindrom.")