# Exploring the Collatz sequence in Python
# Let user type in integer and call function until it returns 1

def collatz(number):
    # Determine if given integer is even or odd
    # Then, commence operations on number
    if (number % 2 == 0):
        result = number // 2
        print(result)
        return result
    elif (number % 2 == 1):
        result = 3 * number + 1
        print(result)
        return result
try:
    # Prompt user input
    n = input('Enter a number: ')

    # Loop until integer reaches 1
    while n != 1:
        n = collatz(int(n))
        
# Handle input validation
except ValueError:
    print('Value Error. Please enter an integer.')
