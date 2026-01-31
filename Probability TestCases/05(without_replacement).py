# Question 5: Independent Again
# Same bag:
# 3 red
# 2 blue
# Two balls are drawn with replacement.
# Probability of both being red?

red = 3
blue = 2
total = red + blue
first = red/total
second = red/total
prob = first * second *100
print(f"Probability : ~{prob:.2f}%")