# import sys module
import sys

# Loop

while True:
    # Prompt user input
    print('Type exit to exit.')
    response = input()

    if response == 'exit':
        # End loop and program
        sys.exit()

    print ('You typed ' + response + '.')
