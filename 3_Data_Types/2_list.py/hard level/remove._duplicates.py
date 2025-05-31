# Remove Duplicates:
# Remove duplicates from the list nums = [1, 2, 2, 3, 4, 4, 5] without using sets.

nums = [1,2,2,3,4,4,5]
print("Original List :",nums)

unique_nums = []
for x in nums:
    if x not in unique_nums:
        unique_nums.append(x)
print("Unique Numbers List :",unique_nums)