# Placeholder list value
catNames = []

# Prompt user input until they give no value.
while True:
    print('Enter the name of cat #' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()

    if name == '':
        break

    # List concatenation
    catNames = catNames + [name]

    print('The cat names are:')

    # Loop over catNames list
    for name in catNames:
        print(' ' + name)
