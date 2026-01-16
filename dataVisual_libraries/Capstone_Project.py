import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IPL.csv')
# print(f"DataSet Has {df.shape[0]} Rows And {df.shape[1]} Columns in Total")

# Now let's see how many columns have null values in total.
# print(df.isnull().sum())

# Which team won the most matches?
# match_wins = df['match_winner'].value_counts()
# sns.barplot(y= match_wins.index , x = match_wins.values,palette='rainbow')
# plt.title('Match Winning Teams')
# plt.tight_layout()
# plt.show()



# Toss Decision Trends
# colors = ['green','red']
# sns.countplot(x = df['toss_decision'],palette=colors)
# plt.title('Toss Decison Trends')
# plt.show()



# Toss Winner vs Match Winner
tossCount = df[df['toss_winner'] == df['match_winner']]
percentage = tossCount.shape[0]/df.shape[0]*100
print(round(percentage,2))


