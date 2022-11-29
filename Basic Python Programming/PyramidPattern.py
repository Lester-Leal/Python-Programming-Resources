# Pyramid Pattern using Python
# Author: Lester Leal

# Function to demonstrate printing pattern
def pypart(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*" * i)
    print(" " * (n-1) + myList[0])
    for i in range(1,n):
        print(" " * (n-i-1) + myList[i] + " " + myList[i])

# Driver Code
n = 5
pypart(n)