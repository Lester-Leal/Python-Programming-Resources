# Python script that takes a string input for remail and check if it
# is a valid email using regex. Redo if invalid and exits script if valid
# Valid email format: any@any.any

# Author: Jorn Blaedel Garbosa

import re

# Define the regex pattern for a valid email address
email_regex = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

# Loop until the user enters a valid email address
while True:
    # Get the email address from the user
    email = input('Enter an email address: ')

    # Check if the email address is valid
    if re.match(email_regex, email):
        # If the email address is valid, break out of the loop
        break
    else:
        # If the email address is not valid, print an error message
        print('Invalid email address. Please try again.')

# Print a success message
print('Valid email address')
