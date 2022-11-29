# Simple Calculator that can do addition, subtraction, multiplication, and division.
# Author: Lester Leal

# Declare variables
num1 = 0
num2 = 0
result = 0
operator = ""

# Get the first number
print("\n+----------------------------------+")
num1 = float(input("Enter the first number: "))
print()

# Get the operator
operator = input("Enter the operator: ")
print()

# Get the second number
num2 = float(input("Enter the second number: "))
print()

# Perform the operation
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("Invalid operator!")

# Display the result
print("The result is: %.2f" % result)
print("+----------------------------------+")