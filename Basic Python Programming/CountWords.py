"""
Author: BogdanOtava

This is a simple implementation of a function that counts the amount of words in a string.
"""

# Create the function
def count_words(string:str):
    # Use the '.split()' method to separate the words by spaces
    words_list = string.split(" ")

    # Print the total amount of words in the list
    print(len(words_list))

# Call the function
count_words("Hello, World!")