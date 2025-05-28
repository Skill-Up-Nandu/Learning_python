# find out the most frequent character
user_input = input("enter your name : ")
if user_input:  # check if string is not empty
     # use set to avoid checking the same character multiple times
     most_frequent = max(set(user_input), key = user_input.count)
     print("The most frequent charcter :",most_frequent)
else:
     print("No input provided") 

