# This is a guess the number game

# import random module
import random

# Store random integer between 1 and 20
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):
    # Prompt user input
    print('Take a guess.')
    guess = int(input())

    # Conditions, else determines correct guess
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break

# End game
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope! The number I was thinking of was ' + str(secretNumber) + '.')
