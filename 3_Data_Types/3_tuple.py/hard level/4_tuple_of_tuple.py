# Tuple of Tuples
# Given this tuple:
# students = (("Alice", 21), ("Bob", 22), ("Charlie", 23))
# Print each student’s name and age.

students = (("Naina", 27), ("Ishu", 25), ("Nandu", 24), ("Gullu", 22))

def new_tuple():
    for idx , (name, age) in enumerate(students, start = 1):
        print(f"{idx}. Name : {name} , Age : {age}")
 
new_tuple()