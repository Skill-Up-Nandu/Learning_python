intro = "* Ah, lists in Python — \nBecause one variable just isn’t enough.\n* Why store one value when you can hoard a whole bunch in square brackets and call it a day?\n* Whether it’s numbers, strings, or your existential crises.\n* Just throw them all into a list! Want to sort them? Slice them? Mutate them like a mad scientist?\n* Python says: Go ahead, break all the rules of tidy programming while you’re at it.\n* Lists: because chaos deserves structure too."
print(intro)

# key point :

1. ADT (Abstract Data Type) -> "Refers to a data structure which we purely know by its behavior (what operations it supports and what results to expect) rather than its implementation (how it's built internally)."

* list is a built-in data type

* It is implemented as a dynamic array, not a linked list

* But it still acts like the list ADT, because it supports the expected   behaviors (insert, delete, index, etc.)

2. It can store elements of different types.

3. Lists are mutubale (we can update any element)



#### METHODS #####

1 .  ADD ELEMENT : 
* list.append(ele)  
        // * [1,2,3]  -> (4) -> [1,2,3,4]
        // * [1,2,3]  -> ([3,4,5])   -> [1,2,3,[3,4,5]]
* list.extend(ele)
        // * [1,2,3]  -> (4) -> [1,2,3,4]
        // * [1,2,3]  -> ([3,4,5])   -> [1,2,3,3,4,5]

2. REMOVE ELEMENT :
* list.remove(el) // remove first occurance of the element.
* list.pop(indx) // remove the element at passed indx.

when you remove elements from a list while iterating over their indices, the list shrinks and the indices shift, causing you to skip or remove the wrong elements.

Correct way:
Iterate over the indices in reverse order or use a list comprehension to create a new list without the unwanted elements.   // i.g delete.py (easy)

