# NESTED TUPLE UNPACKING
# data = ("Jane", (90, 95, 88))


# Unpack name into a variable, and scores into three variables
data = ("Jane", (90, 95, 88))
print(f"Record : {data}")

# unpack nested tuple
name, (sub_1, sub_2, sub_3) = data
print("\nIn Details :")
print(f"* Name : {name}")
print(f"* Marks -")
print(f"    1. Subject_1 : {sub_1}")
print(f"    2. Subject_2 : {sub_2}")
print(f"    3. Subject_3 : {sub_3}")

print("\nAnother Example : \n")
data = ("Jane" , (90,95,88))
print(f"Record : {data}")

# Unpack the outer tuple into 'name' and 'marks'
name , marks = data
print("\nIn Details :")
print(f"* Name : {name}")
print(f"* Marks -")

# Loop through the marks tuple, printing each subject's mark with its index
for idx , mark in enumerate(marks, start =1):
    print(f"    {idx}. Subject_{idx} : {mark}")