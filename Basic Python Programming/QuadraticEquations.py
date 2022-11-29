# Author: Lester Leal

# Declare variables
a = 0
b = 0
c = 0

# Get the values of a, b, and c
print("\n+----------------------------------+")
a = float(input("Enter the value of a: "))
print()
b = float(input("Enter the value of b: "))
print()
c = float(input("Enter the value of c: "))
print()

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Calculate the roots
root1 = (-b + (discriminant ** 0.5)) / (2 * a)
root2 = (-b - (discriminant ** 0.5)) / (2 * a)

# Display the roots
print("The roots are: %.2f and %.2f" % (root1, root2))
print("+----------------------------------+")