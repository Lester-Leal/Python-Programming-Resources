# Payslip for an employee based on their hours worked and hourly rate
# Author: Lester Leal

# Define the variables
hoursWorked = 0
hourlyRate = 0
grossPay = 0
netPay = 0
tax = 0

# Get the number of hours worked
print("\n+----------------------------------+")
hoursWorked = float(input("Enter the number of hours worked: "))
print()

# Get the hourly rate
hourlyRate = float(input("Enter the hourly rate: "))
print()

# Calculate the gross pay
grossPay = hoursWorked * hourlyRate
# Calculate the tax
tax = grossPay * 0.12
# Calculate the net pay
netPay = grossPay - tax

# Display the gross pay
print("The gross pay is: %.2f" % grossPay)
# Display the tax
print("The tax is: %.2f" % tax)
# Display the net pay
print("The net pay is: %.2f" % netPay)
# End of program
print("+----------------------------------+")