# Filter names by filtered_names
# ➤ From names = ['Sam', 'Tommy', 'Alex', 'John'], get names with more than 3 letters.

names = ['sam', 'tommy', 'alex', 'john']
print('List :', names)

# filter by filtered_names od letters more than 3
filtered_names = [name for name in names if len(name) > 3]
print('Filterd List :',filtered_names)

