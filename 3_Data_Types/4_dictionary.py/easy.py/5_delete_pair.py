# Delete the key "City" from the dictionary.

person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai",
    "profession" : "Engineer"
}

def remove_pair_del(del_key):
    del person[del_key]

def remove_pair_pop(del_key):
    person.pop(del_key)


# removes the last pair of dictionary and return them
def remove_pair_pop_item():
    key, value = person.popitem()
    print(f"Removed pair : {key} : '{value}'")

print(f"Original : {person}")
remove_pair_del("profession")
remove_pair_pop("age")
remove_pair_pop_item()

print(f"Updated : {person}")