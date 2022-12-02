# Email Slicer Program
# Author: Lester Leal

# get the email address from the user
email = input("Enter your email address: ")

# slice out the user name
user = email[:email.index("@")]

# slice the domain name
domain = email[email.index("@") + 1:]

# format message
output = "Your username is {} and your domain name is {}".format(user, domain)

# display the output message
print(output)