# Loop through a dictionary and print each key and value.

person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai",
    "profession" : "Engineer"
}

def loop_over_dic():
    for k , v in person.items():
        print(f"Key : {k.title()} , Value : {v}")

loop_over_dic()