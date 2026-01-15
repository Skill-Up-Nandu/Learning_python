import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('tips')
print(df.head())
sns.jointplot(x='tip',y='total_bill',data=df,kind='scatter' )
plt.show()