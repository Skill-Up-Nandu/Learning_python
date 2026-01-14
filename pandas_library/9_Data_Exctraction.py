import pandas as pd
import numpy as np

df = pd.read_csv("Countries.csv")

print(df.info())

# Which country has the highest population

print(f"\n1. Country with the Highest Population : \n{df[df['population'] == df['population'].max()]['country']}")

# What is the capital of the country with highest population

print(f"\n2. Capital of the above country : \n{df[df['population'] == df['population'].max()]['capital_city']}")

# Which country has the least population

print(f"\n3. Country With least Population : \n{df[df['population'] == df['population'].min()]['country']}")

# What is the capital of the country with least population

print(f"\n4. Capital of the above country : \n{df[df['population'] == df['population'].min()]['capital_city']}")

# Give me top 5 countries with highest democratic score

print(f"\n5. Top Five Countries with maximum Democracy Score  : \n{df.sort_values(by='democracy_score',ascending=False).head()['country']}")

# How many total regions are there

print(f"\n6. Total Regions : \n{df['region'].value_counts().count()}")

# How many countries lie in Eastern Europe region

print(f"\n7. Total Countries lies in Eastern Europe : \n{df[df['region'] == 'Eastern Europe']}")

# Who is the political leader of the 2nd highest populated country

# print(f"\n8. Political Leader of Second Highest Populated Country : \n{df.sort_values(by='population',ascending=False)['political_leader'].head(2).tail(1)}")

print(f"\n8. Political Leader of Second Highest Populated Country : \n{df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader']}")

# How many countries are there whoes political leaders are unknown

print(f"\n9. Total Countries with unknown Political Leaders : {df['political_leader'].isna().sum()}\n{df[df['political_leader'].isna()]['country']}")


# How many country have Republic in their full name

count = 0
def counting(country_name) :
    global count

    if 'republic' in country_name.lower() :
        count += 1
    
    return country_name
df['country_long'].apply(counting)
print(f"\n10. Total Countries having Republic in thier name : {count}")

# Which country in african region has highest population

continent_df = df[df['continent'] == 'Africa']
print(f"11. Highest Populated country is : \n{continent_df[continent_df['population'] == continent_df['population'].max()]['country']}") 