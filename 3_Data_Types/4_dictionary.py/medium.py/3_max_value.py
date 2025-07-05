# Find the key with the maximum value in the dictionary:

scores = {'A': 78, 'B': 82, 'C': 91}

def check_maximum() :
    max_key = max(scores , key = scores.get )
    max_value = scores.get(max_key)
    print(f"Maximum Score : {max_value} aggregate by {max_key}")

def check_max():
    max_val = max(scores.values())
    print(f"Maximum Score : {max_val}")

check_maximum()
check_max()


# Step-by-step:
# scores is a dictionary:

# max() function:

# The max() function returns the largest item in an iterable.
# Here, the iterable is the dictionary scores, so it iterates over the keys: 'A', 'B', 'C'.
# key=scores.get:

# The key argument tells max() how to compare items.
# scores.get is a function that, given a key, returns its value from the dictionary.
# So, for each key, max() uses scores.get(key) to get the value.
# How it works:

# For 'A', scores.get('A') → 78
# For 'B', scores.get('B') → 82
# For 'C', scores.get('C') → 91
# max() compares these values and finds the key with the highest value.
# Result:

# max_key will be 'C' because scores['C'] is 91, the highest value.

