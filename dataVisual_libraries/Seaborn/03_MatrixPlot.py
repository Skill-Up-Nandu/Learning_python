import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')
# print(tips.head())

tipscorr = tips[['total_bill','tip','size']]
# print(tipscorr.head())

# tipscorr.corr()

# HEATMAP
sns.heatmap(tipscorr.corr(),annot=True)
plt.show()

# CLUSTERMAP
sns.clustermap(tipscorr.corr())
plt.show()

# PIVOT_TABLE HEATMAP
flights = sns.load_dataset('flights')
# print(flights.head())
flights_pivot = flights.pivot_table(values='passengers',index='month',columns='year')
# print(flights_pivot)
sns.heatmap(flights_pivot)
plt.show()