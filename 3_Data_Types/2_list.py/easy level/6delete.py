# Delete Elements:
# Remove the element "cat" from the list animals = ['dog', 'cat', 'mouse'].

animals = ['dog','cat','mouse']
print("Old List :",animals)

# remove an element by name
animals.remove('cat')
print('Update 1 "Remove" :',animals)

# add an element
animals.append('frog')
print('Update 2 "Append" :',animals)

# remove an element by passing index
animals.pop(1)
print('Update 3 "Pop" :',animals)

# example 2 (ref method.2)
# remove 3 from the list as all indices4

numbers = [2,4,5,3,6,3,7,7,8,3,9,3]
print('Number list :',numbers)

# remove a particular element at all indices
idx_lst = [i for i , num in enumerate(numbers) if num == 3]
print(idx_lst)
for idx in reversed(idx_lst):
    numbers.pop(idx)
print('Updated list (using iteration):',numbers)


# comprehension method
filtered_lst = [ i for i in numbers if i != 3]
print("Updtaed list (using comprehension):",filtered_lst)