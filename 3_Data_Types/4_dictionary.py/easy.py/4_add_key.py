# Add a new key-value pair "Profession": "Engineer".

person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai"
}

def add_new_key_value_pair():
    new_key = input("New Key : ")
    new_value = input("Value : ")
    person.update({new_key : new_value})
    print(f"Updated Dictionery : {person}")


print(f"Old Dictionery : {person}")
add_new_key_value_pair()