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
    // AT THE END
* list.append(ele)  
        // * [1,2,3]  -> (4) -> [1,2,3,4]
        // * [1,2,3]  -> ([3,4,5])   -> [1,2,3,[3,4,5]]
* list.extend(ele)
        // * [1,2,3]  -> (4) -> [1,2,3,4]
        // * [1,2,3]  -> ([3,4,5])   -> [1,2,3,3,4,5]
    
    // AT ANY index
* list.index(idx,ele)


2. REMOVE ELEMENT :
* list.remove(el) // remove first occurance of the element.
* list.pop(indx) // remove the element at passed indx.

when you remove elements from a list while iterating over their indices, the list shrinks and the indices shift, causing you to skip or remove the wrong elements.

Correct way:
Iterate over the indices in reverse order or use a list comprehension to create a new list without the unwanted elements.   // i.g delete.py (easy)

3. REVERSE LIST 
* list.reverse()
* revered.(list)
    // specialy used in removing elements by indices .

4. SORTING
* list.sort()  // result in ascending order
* list.sort(reverse = True)  // result in descending order

5. RETURN Index
* list.index(ele) // return the particular index of the element
        i = list.index(ele)  // store the value return

######################## NEW CONCEPTS ##########################

1. COMPREHENSION 
* List comprehensions are a consice and redable way to create a list or filter a list in python.
* Instead of using loops and .append() method you can easily build a new list in a signle line of code.

    // SYNTAX :
    new_list = [ expression for item in iterable]
    * expression -> what to print (any method , function , operators)
    * item  -> item_name (manualy) in a list
    * iterable  -> list name


2. ENUMERATE 
* The enumerate() function in pyhton is used to loop over iterable (list tuple) and get both the index and the value at the same time.
 // SYNTAX :
    enumerate(iterable , start = num)  // default start from 0
    i.g. comprehension (medium)
** enumerate is cleaner , more readable and pythonic.

3. ENUMERATE INSIDE COMPREHENSION
* Using this you can print both the value and index easily.


3. HOW TO FLATTEN 2D AND 3D LIST
* Using comprehension you can easily flatten the 2d and 3D
  // 2D FLAT LIST 
  -> 1D_list = [item for sublist in 2D_list for item in sublist]

  // 3D FLAT LIST
  -> 1D_list = [item for sublist in 3D_list for subsublist in sublist for item in subsublist]