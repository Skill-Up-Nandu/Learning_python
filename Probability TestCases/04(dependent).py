# Question 4: Dependent Event (Without Replacement)
# A bag contains:
# 3 red balls
# 2 blue balls
# Two balls are drawn one after another without replacement.
# What is the probability that both are red?

red = 3
blue = 2
total = red+blue
first_pick =  red/total
second_pick = (red-1)/(total-1)
prob = first_pick*second_pick
print(f"Both Are Red : {prob*100:.2f}%")