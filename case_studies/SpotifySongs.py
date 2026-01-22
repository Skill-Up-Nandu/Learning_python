import numpy as np
import pandas as pd

df = pd.read_csv(r'artists.csv')
print(df.head())
# print(df.info())
# print(df.describe())
# print(df.shape)
# print(df.columns)


# Four Core Questions :

# 1. What does the landscape look like ?
# que : How many artist are there : 
total_artists = np.array(df['name'].unique())
print(total_artists)

# que : Which genres is dominating :
print(df['genres'].value_counts())


