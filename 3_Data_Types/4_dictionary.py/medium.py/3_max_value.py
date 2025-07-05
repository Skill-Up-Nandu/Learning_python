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

