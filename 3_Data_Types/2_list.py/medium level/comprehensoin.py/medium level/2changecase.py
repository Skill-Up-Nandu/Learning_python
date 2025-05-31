# Convert changecases
# ➤ Given fruits = ['APPLE', 'BaNaNa', 'ChErRy'], return a list of all fruits in differet cases.

fruits = ['APPLE', 'BaNaNa', 'ChErRy']
print('List :', fruits)

#chnage elements into lowercase
lower_case = [fruit.lower() for fruit in fruits]
print('Lower Case :', lower_case)

#chnage elements into uppercase
upper_case = [fruit.upper() for fruit in fruits]
print('Upper Case :', upper_case)

#chnage elements into titlecase
title_case = [fruit.title() for fruit in fruits]
print('Title Case :', title_case)