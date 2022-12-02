# Password Generator - Generates a random password for the user
# Author: Lester Leal

# import the random module
import random

# define the main function
def main():
    # get the length of the password from the user
    length = int(input("Enter the length of the password: "))

    # initialize the password variable
    password = ""

    # loop until the password is the desired length
    while len(password) != length:
        # get a random number from 33 to 126
        char = random.randrange(33, 127)

        # convert the number to a character
        password += chr(char)

    # display the password
    print("Your password is:", password + ".")

# call the main function
main()