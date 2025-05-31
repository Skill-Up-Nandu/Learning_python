# Count and Index:
# Count how many times the number 3 appears in [1, 3, 5, 3, 7, 3, 9] and find its first index.

numbers = [1,3,5,3,7,3,9,3]
print('List :',numbers)
print('Analysis of element 3 :')

# count how many times a particular element occures
count_3 = numbers.count(3)
print("Total Appearance :",count_3)

# retriving the index of a given element
first_idx = numbers.index(3)
print('First Index : ',first_idx)

# retriving all the index of a given element
indices = [idx for idx , num in enumerate(numbers) if num == 3]
print('All indices :',indices)
