# Infinite loop
while True:
    # Prompt user input
    print('Who are you?')
    name = input()

    # Flow control statement to evaluate user input
    # Continue loop and prompt again, otherwise evaluate next step
    if name!= 'Joe':
        continue

    # Next step in loop, prompt user input for password
    # Then, break out of loop
    print('Hello, Joe. What is the password? (Hint: It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
