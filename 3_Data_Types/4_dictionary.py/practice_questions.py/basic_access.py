# Create a dictionary of 3 students with their marks. Print each student's name and marks.

students = {
    'isha' : 89, 'khushi' : 78, 'sunaina' : 96
}

# call the ductionaries item
for stu, marks  in students.items():
    print(f"{stu} scored {marks}")

# Add a new student to the dictionary. Update the marks of an existing student.

students.update({'sameer' : 78})
students.update({'khushi' : 12})
students['akki'] = 45
students['sunaina'] = 75
print(students)

# Ask the user for a student name. Print their marks using `.get()` (return “Not found” if missing).

# name = input("Enter Your Name : ")
# marks = students.get(name)
# if marks is not None:
#     print(f"{name.title()} scored {marks} marks.")
# else:
#     print(f"No record found of {name.title()}.")

# Given a string, count how many times each character appears using a dictionary.

text = input("Enter any string : ")
freq = {}
for char in text :
    freq[char] = freq.get(char, 0)+1
print(freq)
