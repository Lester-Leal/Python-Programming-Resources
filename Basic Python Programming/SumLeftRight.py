# Input 10 numbers, pick a position and computes the sum of items from the left,
# and from the right, except the chosen position

# Author: Jorn Blaedel Garbosa

def print_my_halves(arr, size, pos):
    left_sum = 0
    right_sum = 0
    # Calculate sum of left and right halves
    for i in range(size):
        if i < pos:
            left_sum += arr[i]
        elif i > pos:
            right_sum += arr[i]

    # Print values
    print("Your left has a sum of {}.".format(left_sum))
    print("Your right has a sum of {}.".format(right_sum))


def main():
    arr = [0] * 10
    print("Input 10 numbers")
    # Input numbers
    for i in range(10):
        print("Position {}. ".format(i+1), end='')
        arr[i] = int(input())

    # Ask user for position of division
    print("Enter the position of division: ", end='')
    pos = int(input())

    # Call print_my_halves function
    print_my_halves(arr, 10, pos - 1)


if __name__ == '__main__':
    main()
