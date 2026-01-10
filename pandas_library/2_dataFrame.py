# A pandas DataFrame is two dimensional, size mutable and potentially hetrogeneous tabular data structure with labled aixs (rows / columns).


import numpy as np
import pandas as pd
Emp_details = {
    'Name' :['Nandu','Naina','Ishu','Arnish'],
    'Age': [25,28,26,23],
    'City':['Kurukshtera','Panchkula','Delhi','Chandigharh'],
    'Salary':[15000,12000,45000,20000]
}

# creation with columns 
df = pd.DataFrame(Emp_details)
print(f"Students Details : \n{df}")

mul_list = [['Neeraj','Sahil','Anmol'],['Yogita','Shweta','Akshita'],['Jatin','Vishu','Nidhi'],['Nidhi','Anamika','Sakshi']]

# creation without columns
df2 = pd.DataFrame(mul_list)
print(f"\nFriends List \n{df2}")

# insert any new columns
df['Designation'] = ['Porfessor','Hr Manager','Designer','Sales Executive']
print(f"\nUPdate Employee Details : \n{df}")

# Acccess any column

print(f"\nList of all Employees : \n{df['Name']}")
print(f"\nList of Designation Wise Salaries : \n{df[['Designation','Salary']]}")

# Access any row

print(f"\nDetails of an Employee :\n{df.loc[2]}")

# Subset Access
print(f"\nAny Subset : \n{df.loc[[1,2]][['Age','City']]}")


# Delete any columns

print(df.drop('City',axis=1))
print(f"\nOriginal (Temp) : \n{df}")

# To remove from the original dataFrames

print(df.drop('City',axis=1,inplace=True))
print(f"\nOriginal (Permanent) : \n{df}")

# Delete row

print(df.drop(1))
print(f"\nOriginal (Temp): \n{df}")

# To remove from the original dataFrames

print(df.drop(1,inplace = True))
print(f"\nOriginal (Permanent): \n{df}")

df = pd.DataFrame(Emp_details)

# Conditional Selection

# All employees having age more than 25

print(f"\nABOVE 25 AGED : \n{df[df['Age'] > 25]} ")

# age > 25  and salary must  be above 20000

print(f"\nAbove 25 Aged and Above 20000 Salaried : \n{df[(df['Age']>25) & (df['Salary'] > 20000)]}")