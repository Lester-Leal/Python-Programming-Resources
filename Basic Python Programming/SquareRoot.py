# Find the square root of a number using the Newton-Raphson method.

# Declare variables
number = 0
guess = 0
root = 0

# Get the number
print("\n+----------------------------------+")
number = float(input("Enter the number: "))
print()

# Get the guess
guess = float(input("Enter the guess: "))
print()

# Calculate the root
root = (guess + (number / guess)) / 2

# Display the root
print("The root is: %.2f" % root)
print("+----------------------------------+")