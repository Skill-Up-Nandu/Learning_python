# TUPLE UNPACKING IN LIST COMPREHENSION (ADVANCED)

# Given:
# people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]

# Create a list of strings like: "Alice is 25", "Bob is 30", etc.
# Expected Output: ["Alice is 25", "Bob is 30", "Charlie is 22"]


people = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
print(f"Detail of People : {people}")

# unpack tuple using comprehension
person = [f"{name} is {age}" for (name, age) in people]
print("DETAILS IN PERSON : ")
print(person)