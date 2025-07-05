# Create a dictionary from two lists:

keys = ['name', 'age', 'city']
values = ['Bob', 30, 'Delhi']

def convert_into_dic(keys , values ) :
    zipped = dict(zip(keys , values))
    print(f"Combined Details : {zipped}")

convert_into_dic(keys , values)