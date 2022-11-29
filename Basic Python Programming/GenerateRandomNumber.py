# Generate a random number specified by the user.
# Author: Lester Leal

# Import the random module
import random

# Declare variables
min = 0
max = 0

# Get the minimum and maximum values
print("\n+----------------------------------+")
min = int(input("Enter the minimum value: "))
print()
max = int(input("Enter the maximum value: "))
print()

# Generate the random number
randomNumber = random.randint(min, max)

# Display the random number
print("The random number is: %d" % randomNumber)
print("+----------------------------------+")