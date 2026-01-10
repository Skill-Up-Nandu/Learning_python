import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store': ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales': [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity': [10, 15, 12, 18, 8, 20, 15, 25],
    'Date': pd.date_range('2023-01-01', periods=8)
}
df = pd.DataFrame(data)

print(f"Data : \n{df}")

# Group by Category and calculate the sum of Sales
cat = df.groupby('Category')['Sales'].sum()
print(f"Total Sales by Category : \n{cat}")

# Group by Store and calculate the average of Sales
str = df.groupby('Store')['Sales'].mean()
print(f"Average Sales by Stores : \n{str}")

# Group by multiple columns
# Group by Category and Store

catStr = df.groupby(['Category','Store'])['Sales'].sum()
print(f"Total Sales by Category and Stores : \n{catStr}")

# Aggregation

avgSales = df['Sales'].mean()
print(f"Average Sales : {avgSales}")

print(f"All Aggregations :\n{df['Sales'].agg(['sum','mean','max','min','count','median','std'])}")