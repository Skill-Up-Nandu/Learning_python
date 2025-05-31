# Combine Lists:
# Merge two lists a = [1, 2] and b = [3, 4].

# TIP :
# If you want to avoid modifying the original lists, use the + operator as in flat_method and nested_method.

# using append method
def method_1(lst_1, lst_2):
    lst_1.append(lst_2) # modified the list
    return lst_1

# using extend method
def method_2(lst_1, lst_2):
    lst_1.extend(lst_2) # modified the list
    return lst_1

# append method (add two list as nested manner)
def nested_method(lst_1 , lst_2):
    return lst_1 + [lst_2]  # do not update the list

# extend method (Add two strings as flat manner)
def flat_method(lst_1 , lst_2):
    return lst_1 + lst_2  # do not update the list

# given lists    
a = [1,2]
b = [3,4]
c = [5,6]

# function calls
print(nested_method(a,b))
print(flat_method(a,b))
print(method_1(a,b))
print(method_2(b,c))

