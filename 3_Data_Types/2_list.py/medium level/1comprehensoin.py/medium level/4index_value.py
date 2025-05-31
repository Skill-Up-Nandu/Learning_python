# List of tuples (index, value)
# ➤ From colors = ['red', 'blue', 'green'], create a list like [(0, 'red'), (1, 'blue'), (2, 'green')].

colors = ['red', 'blue', 'green']
print("Original list :", colors)

# cretaing a index value list (using enumerate)
idx_val = [ (idx , color) for idx , color in enumerate(colors)]
print('Index Value Pair : ',idx_val)