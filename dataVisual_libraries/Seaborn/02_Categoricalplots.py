import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# find out quantitative and qualitative columns
df = sns.load_dataset('tips')
print(df.head())

# COUNTPLOT 
# sns.countplot(x = df['sex'],hue=df['smoker'])
# plt.show()


# BARPLOT
# sns.barplot(x=df['sex'] , y=df['tip'],hue=df['sex'],estimator=np.sum)
# plt.show()


# BOXPLOT
# sns.boxplot(x=df['day'] ,y=df['total_bill'],hue=df['sex'])
# plt.show()


# VILONPLOT
# sns.violinplot(x=df['size'],y=df['total_bill'])
# plt.show()


# stripplot
# sns.stripplot(x=df['day'] , y=df['total_bill'])
# plt.show()


# swarnplot
# sns.swarmplot(x=df['day'],y=df['total_bill'],hue=df['sex'])
# plt.show()


# combined vilonplot and swarnplot
sns.violinplot(x=df['day'],y=df['total_bill'],palette='pastel')
sns.swarmplot(x=df['day'],y=df['total_bill'],hue=df['sex'],palette='bright')
plt.show()