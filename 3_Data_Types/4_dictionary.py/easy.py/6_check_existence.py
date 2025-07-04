# Check if the key "Name" exists in the dictionary.


person = {
    "name" : "naina",
    "age" : 25,
    "city" : "Mumbai",
    "profession" : "Engineer"
}

def check_existence(key):

    # convert the key into lower_case to prevent the error 
    key_lower = key.lower()

    # Create a lowercase - keyed version of the dictionary
    person_lower = {k.lower() : v for k , v in person.items()}
    
    if key_lower in person_lower:
        print(f"Yes! It Exist.")

        # to print the value of key 
        want_print = input("Do you want the Value : (yes/no) : ").strip().lower()
        if want_print == "yes":
            print(f"The Value of {key.title()} : {person_lower[key_lower]}")
        else : 
            print("Thanks !")
    else:
        print(f"It doesn't exists.")

check_existence("city")



# What your code does:
# Converts the input key and all dictionary keys to lowercase for case-insensitive lookup.
# Checks if the key exists.
# If it exists, asks the user if they want to see the value and prints it if requested.