# DICTIONARY 
- It is a data structure that allows us to store data in form of key:value pair.
- It is mutable.
- They are of unordered 

# METHODS

- **Extract values**
    - dict.values()

- **Extract keys**
    - dic.keys() // dict_key([key1 , key2 , .....])
    - lis(dic.keys())  // [key1, key2 , key3 ,..........]

- **Use Aggregating Functions**
    - min(dic , key = students.get) // return the key of min value
    - max(dic , key = students.get) // return the key of max value
    - sum(dic.values())
    - average = sum(dic.values()) / len(dic) // average of values

- **Dictionary Unpacking**
    - new_dic = **my_dic 
    # unpacks all key-value pairs from my_dic to new_dic
    - new_dic = {**dic_1 , **dic_2}
    # unpacks all key_value pairs from dic_1 and dic_2 and store them into new_dic

- **Merge Dictionaries**
    - two dictionaries must have unique keys.
    - if both dictionaries have the same key , the value from the second dictionary will overwrites the value from the first.

- **Dictionary Comprehension**
    - result = { "Physics" : 56 , "Chemestry" : 78 , "Maths" : 89 }
    # on accessing - result["physics"] # keyError !
    # since there is no as such key in result ,  because 
    # physics != Physics (case sensitive)

    - A consice way to create a temporary dictionary to make it
      # case Insensitive

    - new_dic = { key_exp : value for key , value in iterable }
    - result_lower = { k.lower() = v for k , v in result.items() }