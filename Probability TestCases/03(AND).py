# Question 3: Two Independent Events
# You toss a coin and roll a die.
# Probability of getting:
# Heads AND
# A 6

head = 1/2
six = 1/6

prob_both = head*six
print(f"Probability of getting Head and Six : {prob_both*100:.2f}%")


# Simulation Check 

import random

trials = 10000
success = 0
for _ in range(trials) : 
    coin = random.choice(['H','T'])
    dice = random.randint(1,6)
    if coin == 'H' and dice == 6 :
        success+=1
# print(coin,dice)
prob = success/trials
print(f"Probability of getting Head and Six : ~{prob*100:.2f}%")