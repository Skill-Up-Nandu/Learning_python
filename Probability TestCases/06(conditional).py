# Question 6: Given That...
# A class has:
# 5 boys
# 7 girls
# One student is chosen randomly.
# Given that the chosen student is a girl,
# What is the probability she wears glasses if 3 girls wear glasses?

boys = 5
girl = 7
total = boys+girl
girls_with_glasses = 3
prob = girls_with_glasses/girl
print(f"Probability (Girls | Glasses)  : {prob*100:.2f}%")