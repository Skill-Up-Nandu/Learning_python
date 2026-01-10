# Merging DataFrame

import numpy as np
import pandas as pd

employees = {
    'Emp_id' : [1,2,3,4,5],
    'Name'  : ['Kapil','Nakkul','Garvit','Jaikant','Rahul'],
    'Age' : [22,23,25,23,26]
}

df1 = pd.DataFrame(employees)

salaries = {
    'Emp_id' : [1,2,3,6,7],
    'Salaries' : [65000,45000,56000,85000,36000,]
}

df2 =pd.DataFrame(salaries)

print(f"Employee : \n{df1}")
print(f"Salaries : \n{df2}")
print(f"Merged Default : \n{pd.merge(df1,df2)}")
print(f"Merged Inner : \n{pd.merge(df1,df2,on='Emp_id',how='inner')}")
print(f"Merged Outer : \n{pd.merge(df1,df2,on='Emp_id',how='outer')}")
print(f"Merged Left : \n{pd.merge(df1,df2,on='Emp_id',how='left')}")
print(f"Merged Right : \n{pd.merge(df1,df2,on='Emp_id',how='right')}")


# Concatenation

dataset1 = pd.DataFrame({
    'A':[101,102,103,104],
    'B':[201,202,203,204]
})

dataset2 = pd.DataFrame({
    'A': [301,302,303,304],
    'B': [401,402,403,404]
})

print(f"DataSet 1 : \n{dataset1}")
print(f"DataSet 2 : \n{dataset2}")
print(f"Concatenate Columns  : \n{pd.concat([dataset1,dataset2],axis=0)}")
print(f"Concatenate Rows  : \n{pd.concat([dataset1,dataset2],axis=1)}")


# Joining

data1 = pd.DataFrame({
    'names' : ['Nandini','Neeraj']
},index=[1,2])
data2 = pd.DataFrame({
    'ages' : [25,24]
},index=[2,3])

print(f"{data1}\n{data2}")
print(data1.join(data2))