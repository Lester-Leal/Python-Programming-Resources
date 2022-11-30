# Basic Fast Food POS
# Author: @artcabrera

# Initialize product variables
productNames = ["Fried Chicken", "Spaghetti", "Hamburger", "French Fries", 
                "Coke Float", "Sundae", "Sisig", "Ice Cream", "Pizza", "Tacos"]
productPrices = [50.00, 80.00, 40.0, 55.0, 35.0, 30.0, 70.0, 90.0, 150.0, 80.0]

# Print the main UI to console
print("\n++++++++++++++++++++++++++++++++")
print('{:>4} {:>16} {:>8}'.format("Code","Product Name","Price"))
print("++++++++++++++++++++++++++++++++")
for i in range(len(productNames)):
    print('{:<4} {:>16} {:>8.2f}'.format(i+1,productNames[i],productPrices[i]))
print("++++++++++++++++++++++++++++++++")

# Ask user to input product choice
choice = int(input("Enter product code: "));

# Ask user to input how many orders of {product choice} they want
quantity = int(input("How many orders of " + productNames[choice-1] + " do you want?: "))

# Calculate the total amount to be paid
total = float(productPrices[choice-1] * quantity)

# Print the total amount
print("\nTotal:", '{:.2f}'.format(total))

# Initialize customer's cash to 0
cash = 0.0

# Loop while cash entered by the user is less than the amount
while (cash < total):
    cash = float(input("Enter customer cash: "))

    # Inform the user if cash is not enough
    if(cash < total):
        print("Cash is not enough!")
    # Calculate and print the change amount
    else:
        print("Thank you! Your change is: {:.2f}".format(cash - total))