import numpy as np
import pandas as pd

data = pd.DataFrame({
    'A' : [5,10,15,20,15],
    'B' : [10,20,30,40,50],
    'C' : [11,22,33,44,55]
},index=[1,2,3,4,5])

print(data)

# apply method

def square(x) : 
    return x**2

data['D'] = data['B'].apply(square)
print(f"Updated : \n{data}")


# basic operations

print(f"\nShape : {data.shape}")
print(f"\nColumns : \n{data.columns}")
print(f"\nInformation : \n{data.info()}")
print(f"\nDescribe : \n{data.describe()}")
print(f"\nBroadcast : \n{data['A'] + 5}")
