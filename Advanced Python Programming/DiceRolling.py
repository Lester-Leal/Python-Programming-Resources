# Dice Rolling Program
# Author: Lester Leal

import random

# define the main function
def main():
    # create a list of 13 elements to hold the counts
    # of the number of times each number comes up
    # the list will be indexed from 1 to 12
    # so the first element is not used
    counts = [0] * 13

    # roll the dice 1000 times
    for i in range(1000):
        # get two random numbers from 1 to 6
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)

        # add the two numbers together to get the total
        total = die1 + die2

        # increment the appropriate element of the counts list
        counts[total] += 1

    # print the results
    print("Face\tFrequency")
    for i in range(2, 13):
        print(i, "\t", counts[i])

main()
