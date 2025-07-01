# logical operators

# AND

x = 10
y = 5
print(f"{x} < 5 and {y} < {x} : ", x < 5 and y < x)

# OR

print(f"{x} < {20} or {y} > {x} : ", x < 20 or y > x)

# NOT

print(f"NOT of 1st statement : {not(x < 5 and y < x)}")
print(f"NOT of 2nd statement : {not(x < 20 or y > x)}")

# demo

age = int(input("Enter Your age : "))
user_input = input("Do have license (yes/no) : ").lower().strip()
have_licensed = True if user_input == "yes" else False

if age >= 18 and have_licensed:
    print("You can drive.")
else:
    print("You are not able to drive")