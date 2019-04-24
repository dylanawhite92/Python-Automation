# Import random module
import random

# Defining function

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain.'
    elif answerNumber == 2:
        return 'It is decidedly so.'
    elif answerNumber == 3:
        return 'Yes.'
    elif answerNumber == 4:
        return 'Reply hazy, try again.'
    elif answerNumber == 5:
        return 'Ask again later.'
    elif answerNumber == 6:
        return 'Concentrate, and ask again.'
    elif answerNumber == 7:
        return 'My reply is no.'
    elif answerNumber == 8:
        return 'Outlook not so good.'
    elif answerNumber == 9:
        return 'Very doubtful.'

# Store random int in variable r
r = random.randint(1,9)

# Store function in variable for brevity
# Pass random int with each function call
fortune = getAnswer(r)

# Call function
print(fortune)
