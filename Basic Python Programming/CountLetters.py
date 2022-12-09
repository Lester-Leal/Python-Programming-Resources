"""
Author: BogdanOtava

This is a simple function that counts only the letters (A-Z) in a string.
"""

import string

# Create a list of all the letters (lowercase & uppercase) using list comprehension
ALPHABET = [i for i in string.ascii_letters]

# Create the function
def count_letters(string:str):
    # Variable for the total amount of letters in string
    total = 0

    # Loop through the string and add to total every time there's a letter in the string
    for char in string:
        if char in ALPHABET:
            total += 1

    return total

# Call the function
print(count_letters("Hello World!"))
