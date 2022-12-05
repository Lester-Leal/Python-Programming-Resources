# Rank Average // Emulate excel's RANK.AVG function
# This code calculates and prints the ranks of a group of people based on their grades.
# It does this by first asking the user for 5 grades and storing them in a list.
# The grades are then sorted in descending order, and the number of occurrences
# of each grade is counted. The sum of ranks for each grade is calculated, and the
# average rank is determined by dividing the sum of ranks by the number of occurrences
# of the grade. Finally, the code prints the rank for each person based on their grade.

# Author: Jorn Blaedel Garbosa

# Create an empty list to store the grades
grades = []

# Ask the user for 5 grades
for g in range(5):
    # Print a prompt and store the grade in the list
    print('Input grade of {0}: '.format(g+1), end=' ')
    grades.append(float(input()))

# Sort the grades in descending order
grades.sort(reverse=True)

# Create an empty list to store the counts of each grade
counts = []

# Count the number of occurrences of each grade
for i in range(len(grades)):
    counts.append(grades.count(grades[i]))

# Initialize the previous grade to the first element in the list
prev = grades[0]

# Create an empty list to store the sums of the ranks for each grade
sums = []

# Initialize the sum of ranks to 1
sum = 1

# Iterate over the remaining elements in the list
for i in range(1, len(grades)):
    # If the current grade is different from the previous one,
    # append the sum of ranks to the list and reset the sum
    if prev != grades[i]:
        sums.append(sum)
        prev = grades[i]
        sum = i + 1
    # If the current grade is the same as the previous one,
    # increment the sum of ranks by the current index
    else:
        sum += i + 1

# Append the final sum of ranks to the list
sums.append(sum)

# Initialize the index to 0
j = 0

# Create an empty list to store the ranks
ranks = []

# Append the average rank for the first grade to the list
ranks.append(sums[0] / counts[0])

# Set the previous grade to the first element in the list
prev = grades[0]

# Iterate over the remaining elements in the list
for i in range(1, len(grades)):
    # If the current grade is different from the previous one,
    # increment the index and update the previous grade
    if prev != grades[i]:
        prev = grades[i]
        j += 1
    # Append the average rank for the current grade to the list
    ranks.append(sums[j] / counts[i])

# Iterate over the grades and print the rank for each one
for i in range(len(grades)):
    print('Person with grade {0} is in Rank {1}'.format(grades[i], ranks[i]))
