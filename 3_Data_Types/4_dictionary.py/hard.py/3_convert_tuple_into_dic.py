# Convert a list of tuples to a dictionary:
# [('a', 1), ('b', 2), ('c', 3)]

my_tup = [('a', 1), ('b', 2), ('c', 3)]

def convert_dict():
    my_dict = {}
    for key , value in my_tup:
        my_dict[key] = value
    print(my_dict) 

def convert_dict_method():
    my_dict = dict(my_tup)
    print(my_dict)

convert_dict()
convert_dict_method()