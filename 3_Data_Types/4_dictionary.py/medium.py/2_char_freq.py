# Count character frequency in a given string using a dictionary.
# Example: Input = "banana" → Output = {'b': 1, 'a': 3, 'n': 2}

user_input = input("Enter any string : ")
def check_char_freq(text):
    freq = {}
    for char in text :
        freq[char] = freq.get(char , 0 ) + 1
    print(f"\nCharacter frequency : {freq}")

check_char_freq(user_input)

# Count word frequency in a sentence using dictionary

sentence = "I love Python and i love coding in Python"

def check_word_freq() :
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word , 0 ) + 1
    print(f"\nWords frequency : {frequency} ")

check_word_freq()
