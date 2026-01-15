import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# find out quantitative and qualitative columns
df = sns.load_dataset('tips')
print(df.head())
print(df.columns)
print(df['size'].unique())

# basic creation of histogram  // kde = kernal density estimator
# sns.histplot(df['total_bill'],bins =10,kde=True)
# plt.show()

# using subplots
plt.subplot(1,2,1)
sns.histplot(df['tip'],kde=True)
plt.subplot(1,2,2)
sns.histplot(df['total_bill'],kde=True)

plt.tight_layout()
plt.show()