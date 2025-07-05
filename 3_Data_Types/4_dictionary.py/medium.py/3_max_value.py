# Find the key with the maximum value in the dictionary:

scores = {'A': 78, 'B': 82, 'C': 91}

def check_maximum() :
    max_key = max(scores , key = scores.get )
    max_value = scores.get(max_key)
    print(f"Maximum Score : {max_value}")

check_maximum()

