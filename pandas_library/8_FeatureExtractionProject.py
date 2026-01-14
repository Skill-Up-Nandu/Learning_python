import numpy as np
import pandas as pd

df = pd.read_csv(r'anime.csv')

## Que 1 : Make a new column for episode count

def extract_episod(txt):
    episods = ""
    check = False
    for i in txt :
        if i == ')':
            check = False
            return episods
        if check == True : 
            episods = episods + i
        if i == '(':
            check = True
    

df['Episods'] = df['Title'].apply(extract_episod)
df['Episods'] = df['Episods'].str.replace(' eps','')
df['Episods'] = df['Episods'].astype('int')
print(f"\n{df.head()}")
# print(type(df.loc[0]['Episods']))



## Que : 2 Make a new column for time stamp

print(df.loc[1]['Title'])

def extraction_time(txt) :
    for i in range(len(txt)) : 
        data = ''
        if txt[i] == ')' :
            for j in range(i+1 , i+20) :
                data += txt[j]
            return data

df['Total Time'] = df['Title'].apply(extraction_time)   

from datetime import datetime

def calculate_total_months(duration):
    """
    Input: 'Apr 2009 - Jul 2010'
    Output: total months (int)
    """
    try:
        start_str, end_str = duration.split(' - ')
        
        start_date = datetime.strptime(start_str, "%b %Y")
        end_date = datetime.strptime(end_str, "%b %Y")
        
        total_months = (end_date.year - start_date.year) * 12 + \
                       (end_date.month - start_date.month) + 1
        
        return total_months
    except Exception:
        return None
    
df['Total Months'] = df['Total Time'].apply(calculate_total_months)
print(f"\n{df.head()}")

## Que : 3 Which anime has the highest score

print(f"\nHighest Score : \n{df[df['Score'] == df['Score'].max()]}")


## Que : 4 Give me top 5 highest scoring anime

print(f"\nTop Five Highest Scoring Anime : \n{df.head()}")
# only anime name
print(f"\nTop Five Highest Scoring Anime : \n{df['Title'].head()}")


## Que : 5 Which anime has the highest episode count

print(f"\nAnime has the highest episode count  :\n{df[df['Episods'] == df['Episods'].max()]}")


## Que : 6 Animes with top 5 episode count

print(f"\nAnimie with top 5 Episods count : \n{df.sort_values(by='Episods', ascending=False).head()}")

## Que : 7 Which is the longest running anime

print(f"Longest Running Anime : \n{df[df['Total Months'] == df['Total Months'].max()]}")