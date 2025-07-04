# Get all keys and values from the dictionary using appropriate methods.

person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai",
    "profession" : "Engineer"
}

def get_keys():
    print(f"All Keys : {list(person.keys())}\n")

def get_values():
    print(f"All Values : {list(person.values())}\n")

def get_key_value_pair():
    print(f"All Key_Value Pairs : {list(person.items())}\n")

get_keys()
get_values()
get_key_value_pair()