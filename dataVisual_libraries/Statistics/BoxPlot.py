# BoxPlot Using : Five Number Summary 
# 1. Minimum
# 2. First Quartile Q1
# 3. Second Quartile Q2
# 4. Third QUartile Q3
# 5. Maximum

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arr = np.array([2,3,4,6,7,8,9,12,13,16,17,23,25,27,34,37,201])
print(arr)
Q1 = np.percentile(arr,25)
Q2 = np.percentile(arr,50)
Q3 = np.percentile(arr,75)
IQR = Q3-Q1
UF = Q3+(1.5*IQR)
LF = Q1-(1.5*IQR)
l=[]
for i in arr :
    if i >= LF and i <= UF :
        l.append(i)
arr2 = np.array(l)
print(arr2)
fig , axs = plt.subplots(1,2,figsize=(16,9))
sns.boxplot(x=arr,palette='rainbow',ax=axs[0])
axs[0].set_title('Having Outliers')
sns.boxplot(x=arr2,palette='pastel',ax=axs[1])
axs[1].set_title('NO Outliers')
plt.tight_layout()
plt.show()