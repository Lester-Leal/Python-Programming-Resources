# IMPORTANT: (IF USING PROVIDED words.txt) DO NOT RUN SCRIPT IN POOR CPU AS THIS SCRIPT ITERATES (NOT JUST ONCE)
# TROUGH A FILE THAT CONTAINS HUNDREDS OF THOUSAND OF WORDS
# Python script that takes an input string of random letters and make words out of it
# NOTE: Need words.txt for this script to work. Create your own with fewer words or download file below
# File can be downloaded here: https://raw.githubusercontent.com/dwyl/english-words/master/words.txt
# words.txt must be in the same folder with the script

# Author: Jorn Blaedel Garbosa

import itertools

# Get the input string from the user
input_string = input('Enter a string of random letters: ')

# Create a list of all possible combinations of the input string
combinations = list(itertools.permutations(input_string))

# Open the file containing the list of valid words
with open('words.txt') as words_file:
    # Read all the words from the file
    words = words_file.readlines()
    # Remove the newline character from each word
    words = [word.strip() for word in words]

# Create an empty list to store the valid words
valid_words = []

# Loop through all the combinations of the input string
for combination in combinations:
    # Convert the combination tuple to a string
    word = ''.join(combination)
    # If the word is a valid word, add it to the list of valid words
    if word in words:
        valid_words.append(word)

# Print the list of valid words
print(valid_words)
