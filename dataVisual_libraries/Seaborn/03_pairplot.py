import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('tips')
print(df.head())

# for analyzing entire data
sns.pairplot(df,hue='sex')
plt.show()


# rugplot 
sns.rugplot(df['tip'])
plt.show()