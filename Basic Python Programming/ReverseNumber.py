# The program will ask the user to input a number and then display the reverse of the number.
# Author: Lester Leal

# Declare variables
number = 0
reverse = 0
temp = 0

# Get the number
print("\n+----------------------------------+")
number = int(input("Enter the number: "))
print()

# Reverse the number using a while loop
temp = number
while temp != 0:
    reverse = (reverse * 10) + (temp % 10)
    temp = temp // 10

# Display the reverse of the number
print("The reverse of the number is: %d" % reverse)
print("+----------------------------------+")
