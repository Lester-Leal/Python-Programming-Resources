# This program will ask the user to input a number and then tell the user if the number is odd or even.
# Author: Lester Leal

# Declare variables
number = 0

# Get the number
print("\n+----------------------------------+")
number = int(input("Enter the number: "))
print()

# Check if the number is odd or even
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Display the number
print("The number is: %d" % number)
print("+----------------------------------+")