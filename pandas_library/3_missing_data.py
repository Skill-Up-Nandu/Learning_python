#  Handling NaN values in dataframes

import numpy as np
import pandas as pd

data = {
    'A' : [1,5,6,9,7],
    'B' : [5,8,np.nan,6,4],
    'C' : [6,np.nan,4,2,np.nan],
    'D' : [8,9,np.nan,4,np.nan]
}

df = pd.DataFrame(data)
print(f"DataSet : \n{df}")

# finding missing data
print(f"\nIs Data is miising : \n{df.isna()}")

print(f"\nCount of missing Data :\n{df.isna().sum()}")

print(f"\nAny missing : \n{df.isna().any()}")


# Removing missing data

print(f"\nRemove all rows having null values : \n{df.dropna()}")

# Removing with conditions

print(f"\nRemove only rows which have two null values  :\n{df.dropna(thresh=3)}")

# Replace with another values

print(f"\nREplace with 0 : \n{df.fillna(0)}")

# Replace each column with different values
vals = {'A' : 'N/A' , 'B' : '0' , 'C' : '-' , 'D': '**'}
print(f"Replace wuth dif values : \n{df.fillna(value=vals)} ")