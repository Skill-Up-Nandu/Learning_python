# Use Tuple  Unpacking in a Loop
# students = [("Tom", 80), ("Jerry", 90), ("Spike", 85)]
# Use a for-loop to unpack and print:
# Name: Tom, Score: 80

students = [("Tom", 80), ("Jerry", 90), ("Spike", 85)]
print(f"All Students Record : {students}")

# unpacking using loop
print("\nIndividual Record (inside loop)")
for idx , tup in enumerate(students, start =1):
    name , score = tup
    print(f"{idx}. Name : {name} , Score : {score}")

# unpacking directly in loop
print("\nIndividual Record (directly in loop)")
for idx , (name , score) in enumerate(students):
    print(f"{idx}. Name : {name} , Score : {score}")