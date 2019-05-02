## Using keywords 'not' and 'in' on list values

# List of pets
myPets = ['Zophie', 'Pooka', 'Fat-tail']

# Prompt user input, handle if they don't capitalize name
print('Enter a pet name:')
name = input().capitalize()

# Check given value against list of pet names
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet!')
