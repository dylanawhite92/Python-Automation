## Magic 8 Ball program, but this time using the list data structure

# import random module
import random

# Store all possible values in a list
messages = ['It is certain.',
            'It is decidedly so.',
            'Yes, definitely.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Concentrate and ask again.',
            'My reply is no.',
            'Outlook not so good.',
            'Very doubtful...']

# Return random message from messages list
print(messages[random.randint(0, len(messages) - 1)])
