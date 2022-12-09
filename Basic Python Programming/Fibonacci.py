"""
Author: BogdanOtava

This is a simple implementation of the 'Fibonacci Sequence'. 
The 'Fibonacci Sequence' is a set of steadily increasing numbers where each number is equal to the sum of the preceding two numbers.

The sequence always starts with 0 and 1, with the first few values being:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
"""

# Ask for input
numbers = int(input("Type how many numbers should be in the sequence: "))

# Create the function 
def fibonacci_sequence(end_point:int):
    """
    Returns the fibonacci numbers up to the 'end_point'.
    """

    # Declare the variables
    first_number, seconds_number, third_number = 0, 1, 0

    # Loop from 0 to end point given as input
    for _ in range(first_number, end_point):
        # Print the third number which at first is 0, and then will be the sum of the two previous numbers.
        print(third_number)
    
        first_number = seconds_number
        seconds_number = third_number
        third_number = first_number + seconds_number

# Call the function
fibonacci_sequence(end_point=numbers)
