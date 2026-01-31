# Question 1: Single Pick Probability

# A jar has:

# 4 green balls

# 6 yellow balls

# You pick one ball randomly.

# What is the probability of picking a green ball?

green_balls = 4
yellow_balls = 6
total_outcomes = green_balls+yellow_balls
green_prob = green_balls/total_outcomes

print(f"Probability of picking a green ball : {green_prob*100}%")