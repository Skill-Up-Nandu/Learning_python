# List Slicing:
# Print the middle three elements of the list nums = [1, 2, 3, 4, 5, 6, 7].

nums = [1,2,3,4,5,6,7,8,9,10,11,12,18]
count = len(nums)
position = (count-1) // 2 # ineteger division for middle position

# slicing to get the middle three elements
print("Middle three elements are : ",nums[position-1:position+2]) 
# last value of slicing is exclusive