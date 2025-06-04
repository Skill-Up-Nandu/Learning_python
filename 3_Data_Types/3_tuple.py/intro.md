# TUPLE

- A built in data type that allows us to store an immutable sequence of data.
my_tup = (element1,element2......)

# KEY CONCEPTS

- ORDERED -> Elements keep the same order.
- IMMUTABLE -> You can not ADD , UPDATE , REMOVE any item.
- ALLOW DUPLICATE -> Like list duplicates are allowed.
- INDEXABLE -> We can access element by index.


✅ Concepts Learned from Practice Questions (Tuples)

🔹 Basic Concepts

- Tuples are orders and immutable collections.
- Defined using () or commas : t = (1, 2, 3) or t = 1, 2, 3
- Use (1, ) for single-element tuple (comma is required).

🔹 2. Tuple vs List

- Tuples : immutable (cannot add, delete, or change items).
- Lists: mutable (can modify elements)
- tuples are faster and safer for fixed data.

🔹 2. Tuple vs List

- Use indexing : t[0], slicing t[1:3]
- supports nested indexing t[2][1] if element are sub tuples/lists.

🔹 4. Tuple Methods

- count(value) - how many times value appears.
- index(value) - position of the first occurence.

🔹 4. Tuple Methods

- let(t) - number of itmes.
- max(t), min(t), sum(t) - for numeric tuples.
- tuple(list_obj) - convert list to tuple.

🔹 6. Tuple Unpacking

- Assign value to variables directly: 
a, b = (10,20)

- Use * to collect etra values:
a, *b, c = (1,2,3,5,6,4,8)
# a = 1
# b = 2,3,5,6,4
# c = 8

🔹 7. Unpacking in Loops & Comprehensions

- in for loops:
for a,b in [(1,2),(3,4),(5,6)]:
    print(a+b)

- in list comprehensions:
[f"{name} is {age}" for name, age in people]

🔹 8. Swapping 

- swapping variable quickly using unpacking :
x, y = y, x

- swapping tuples quickly using unpacking :
a = (1,3,4)   b =(9,8,7)
a, b = b, a

🔹 9. Nested Tuples

- Tuples can contain other tuples or lists:
t = ("john", (90,80,70), 56)

🔹 10. When to Use Tuples

- When data should not change
- As keys in dictionaries
- When working with fixed records (i.g. coordinates, database rows)