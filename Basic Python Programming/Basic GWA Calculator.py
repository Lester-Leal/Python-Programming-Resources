# Simple GWA Calculator
# Author: Lester Leal

# Declare variables
units = 0
grade = 0
totalUnits = 0
totalGrade = 0
gwa = 0

# Get the number of subjects
print("\n+----------------------------------+")
numOfSubjects = int(input("Enter the number of subjects: "))
print()

# Loop through the number of subjects
for i in range(numOfSubjects):
    # Get the units and grade of the subject
    units = int(input("Enter the number of units: "))
    grade = float(input("Enter the grade: "))
    print()

    # Calculate the total units and total grade
    totalUnits += units
    totalGrade += (units * grade)

# Calculate the GWA
gwa = totalGrade / totalUnits

# tell if the student is passed or failed
if gwa >= 75:
    print("You passed the semester! :)")
else:
    print("You failed the semester! :(")
    
# Display the GWA limit to 2 decimal places
print("The GWA is: %.2f" % gwa)
print("+----------------------------------+")

# End of program