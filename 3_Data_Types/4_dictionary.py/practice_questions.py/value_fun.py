# Find the student with the highest marks from a dictionary.

students = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
marks = []
for name, mark in students.items():
    mark = students.get(name)
    marks.append(mark)
print(max(marks))
    
