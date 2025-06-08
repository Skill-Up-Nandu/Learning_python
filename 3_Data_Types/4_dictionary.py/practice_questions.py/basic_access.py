# Create a dictionary of 3 students with their marks. Print each student's name and marks.

students = {
    'isha' : 89, 'khushi' : 78, 'sunaina' : 96
}

for stu, marks  in students.items():
    print(f"{stu} scored {marks}")
