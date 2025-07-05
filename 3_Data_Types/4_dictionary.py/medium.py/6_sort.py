# Sort a dictionary by:
# Key (alphabetically)
# Value (numerically)

marks = {
    "John": 82,
    "Alice": 91,
    "Bob": 78,
    "Daisy": 85
}

def sort_alph():
    sorted_marks = dict(sorted(marks.items()))       
    print(sorted_marks) 

# def sort_nums():
#     sprted_marks = dict(sorted())

sort_alph()
# sort_nums()