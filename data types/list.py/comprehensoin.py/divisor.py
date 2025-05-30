# Numbers divisible by both 3 and 5
# ➤ Create a list of numbers from 0 to 100 that are divisible by both 3 and 5.

divisible_by_3_5 =[num for num in range(101) if num % 3 == 0 and num % 5 == 0]
print("list : ",divisible_by_3_5)