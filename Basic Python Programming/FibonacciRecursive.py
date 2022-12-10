"""
Author: BogdanOtava

This is a simple implementation of the 'Fibonacci Sequence' using recursion.
The 'Fibonacci Sequence' is a set of steadily increasing numbers where each number is equal to the sum of the preceding two numbers.

The sequence always starts with 0 and 1, with the first few values being:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...

'Recursion' is the ability for a function to call itself directly or indirectly.
A recursive function solves a particular problem by calling a copy of itself and solving smaller subproblems of the original problems.

An important aspect of recursion is that we should provide a certain case in order to terminate the recursion process.
"""

# Ask for input
numbers = int(input("Type how many numbers should be in the sequence: "))

# Create the function
def fibonacci_sequence(end_point:int):
    """
    Returns the fibonacci numbers up to the 'end_point'.
    """

    # Provide the base case 
    if end_point <= 1:
        return end_point

    # Get the numbers in the sequence using recursion
    return fibonacci_sequence(end_point - 1) + fibonacci_sequence(end_point - 2)

# Call the function
for i in range(numbers):
    print(fibonacci_sequence(i))
