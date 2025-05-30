# Even numbers from a list
# ➤ From a list nums = [1, 2, 3, 4, 5, 6, 7, 8, 9], create a list of even numbers.

nums = [1,2,3,4,5,6,7,8,9]
print('Original List :',nums)

# retriving even number list
even_nums = [x for x in nums if x % 2 == 0]
print('Even numbers : ',even_nums)