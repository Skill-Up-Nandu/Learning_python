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