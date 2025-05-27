# remove all spaces from a string
user_input = input("Share any thought : ")
print("Original : ",user_input)
char = ""
for el in user_input:
    if el != " ":
        char += el
print(user_input,"withot space : ",char)

# usinh built-in method
user_input.replace(" ","")
print(user_input,"withot space : ",char)