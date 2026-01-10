# Series 

# A Series is a one dimensional labled array , whcih is capable of holding any data type.
# The axis lables are collectively called th index.

import pandas as pd
import numpy as np

my_list = [10,20,30,40]
arr = np.array([50,60,70,80])
index = ['a','b','c','d']
dict = {
    'name':'nandu','roll':61,'course':'mca'
}
my_series= pd.Series(arr)
print(my_series)
my_series2 = pd.Series(my_list)
print()
print(my_series2)
my_series3 = pd.Series(arr,index=index)
print()
print(my_series3)
my_series4 = pd.Series(dict)
print()
print(my_series4)
