# Count character frequency in a given string using a dictionary.
# Example: Input = "banana" → Output = {'b': 1, 'a': 3, 'n': 2}

user_input = input("Enter any string : ")
def check_freq(text):
    freq = {}
    for char in text :
        freq[char] = freq.get(char , 0 ) + 1
    print(freq)

check_freq(user_input)