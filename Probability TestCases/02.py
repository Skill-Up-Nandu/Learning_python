# Question 2: OR Probability

# A deck has cards numbered 1 to 10.

# You pick one card randomly.

# What is the probability of picking a card that is:

# Even OR

# Greater than 7

# import numpy as np

# cards = np.array(range(1,11))
# even_count = 0
# greater_seven = 0
# overlap_count = 0
# for card in cards:
#     if card % 2 == 0 :
#         even_count+=1
#     if card > 7 :
#         greater_seven+=1
#     if card%2==0 and card>7:
#         overlap_count+=1

# # print(even_count)
# # print(greater_seven)
# print(overlap_count)

# total_prob = cards.size
# # print(total_prob)

# even_prob = even_count/total_prob
# greater_seven_prob = greater_seven/total_prob
# overlap_prob = overlap_count/total_prob

# probability = even_prob + greater_seven_prob-overlap_prob
# print(f"Probability of picking a card (Even or Seven): {probability*100:.2f}%")


# better way 

cards = set(range(1,11))
# print(cards)
even = {c for c in cards if c%2==0}
gt7 = {c for c in cards if c>7}
# print(even , gt7)
union = even | gt7
probability = len(union) /len(cards)
print(f"Cards staisfying Conditions : {union}")
print(f"Probability of picking a card (Even or Seven): {probability*100:.2f}%")
