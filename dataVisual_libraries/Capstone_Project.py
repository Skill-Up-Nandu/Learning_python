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
# tossCount = df[df['toss_winner'] == df['match_winner']]
# percentage = tossCount.shape[0]/df.shape[0]*100
# print(round(percentage,2))



# How do teams win? (Runs vs Wickets)
# sns.countplot(x = df['won_by'],hue=df['won_by'],legend=False)
# plt.title('Teams Win BY')
# plt.ylabel('Matches')
# plt.show()



# Most "Player of the Match" Awards
# mof_counts = df['player_of_the_match'].value_counts().head(10)
# sns.barplot(y=mof_counts.index , x=mof_counts.values ,palette='pastel')
# plt.title('Top Ten Man OF The Match Winners')
# plt.tight_layout()
# plt.show()



# 2 Top Scorers
# top_scorer = df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(2)
# print(top_scorer)
# top_scorer.plot(kind='barh')
# plt.title('Top Two Scorer')
# plt.tight_layout()
# plt.show()



# 10 Best Bowling Figures
# df['total_wickets'] = df['best_bowling_figure'].apply(lambda x : x.split('--')[0])
# df['total_wickets'] = df['total_wickets'].astype(int)
# bowling_figs = df.groupby('best_bowling')['total_wickets'].sum().sort_values(ascending=False).head(10)
# print(df.sort_values(by='total_wickets')[['best_bowling','best_bowling_figure']].head(10))
# sns.barplot(x = bowling_figs.values , y=bowling_figs.index,palette='pastel')
# plt.title('10 Best Bowling Figures')
# plt.tight_layout()
# plt.show()




# Most Matches Played by Venue
# venues = df['venue'].value_counts()
# print(venues)
# sns.barplot(x = venues.values ,y = venues.index ,hue=venues.values,legend=False)
# plt.tight_layout()
# plt.title('Most Matches Played By Venue')
# plt.show()




#  Who won the highest margin by runs?
# print(df[df['won_by'] =='Runs'].sort_values(by='margin',ascending=False)[['match_winner','won_by','margin']].head(1))




# Which player had the highest individual score?
# print(df[df['highscore'] == df['highscore'].max()][['top_scorer','highscore']])



# Which bowler had the best bowling figures?
df['total_wickets'] = df['best_bowling_figure'].apply(lambda x : x.split('--')[0])
df['total_wickets'] = df['total_wickets'].astype(int)
print(df[df['total_wickets'] == df['total_wickets'].max()][['best_bowling','best_bowling_figure']])