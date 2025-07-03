# Find the student with the highest marks from a dictionary.

students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# concept 1 : get only maximum of values
print(max(students.values())) 

# concept 2 : key name with having the maximum of values  
print(max(students , key = students.get))

# max key value pair
topper = max(students , key = students.get)
print(f"TOPPER : {topper} with aggregating {max(students.values())} Marks.")

    
