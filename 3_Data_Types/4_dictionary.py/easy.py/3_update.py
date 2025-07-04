# Update the "Age" of Alice to 26.

person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai"
}

def update_age():
    new_age = int(input("Enter new age : "))
    person["age"] = new_age
    print(f"\nUpdated Age : {person['age']}")

print(f"\nAGE : {person['age']}")
update_age()
