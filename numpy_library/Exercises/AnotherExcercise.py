import numpy as np

# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])

# Q1. Get the shape of the matrix.
print(f"\nShape of data is : {data.shape}")

# Q2. Find the average age of students.
age = data[:,0]
avg = np.average(age)
print(f"\nAverage Age : {avg}")
# print(f"Average Age : {np.average(data[:,0])}")

# Q3. Extract Math marks of all students.

math_marks = data[:,1]
print(f"\nMath Marks : {math_marks}")

# Q4. Find the highest Science mark.
max_science = data[:,2].max()
print(f"\nHighest Score of Science : {max_science}")


# Q5. Get details of the student who scored more than 90 in Math.

print(f"\nStudent details who score more than 90 in math : \n{data[data[:,1] > 90]}")

# alt :
# new_data = data.copy()
# bool_indexing = data[:,1] > 90 
# new_data = new_data[bool_indexing]
# print(f"Student details who score more than 90 in math : \n{new_data}")

# Q6. Increase Math marks of all students by 5.


print(f"\nMaths Marks : {math_marks}")
math_marks = math_marks+5
print(f"\nUpdated Maths Marks : {math_marks}")
# alt:
# print(f"\nUpdated Maths Marks : {data[:,1] + 5}")


# Q7. Find how many students are younger than 19.

ageData = data.copy()
bool_index = ageData < 19
ageData = ageData[bool_index]
print(f"\nYounger Students count : {len(ageData)}")

# Q8. Calculate the average marks in each subject (column-wise mean).

avg_math = math_marks.mean() #updated with 5 marks
sci_marks = data[:,2]
avg_sci = sci_marks.mean()
print(f"\nMaths Average : {avg_math.round(2)}")
print(f"Science Average : {avg_sci.round(2)}")
# alt :
print(f"Average of Math and sci respectively : {np.mean(data[:,1:],axis = 0)}")

# Q9. Get data of students who scored at least 80 in both subjects.
print(f"\nStudents who score at least 80 in both sub : \n{data[(data[:,1] >=80) & (data[:,2] >=80)]}")


# Q10. Replace all Science marks < 75 with 0.
for i in range(0,5) :
    for j in range(0,3) :
        if data[i,2] < 75 :
            data[i,2] = 0

print(f"\nUpdated Science Marks \n{data}")

# alt :
# data[:,2][data[:,2] < 75 ] = 0
# print(data)