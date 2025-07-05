# Write a program to swap keys and values in a dictionary.

person = {
    "name" : "Naina" ,
    "age" : 27,
    "city" : "Ambala" ,
    "Profession" : "HR Associative"
}

def swap_key_value():
    swapped = {v : k for k , v in person.items()}
    print(f"Swapped : {swapped}")

swap_key_value()




