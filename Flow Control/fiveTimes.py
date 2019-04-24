# Loop through five times, using either a for or a while loop

print('My name is')

# As a for loop

# i + 1 to offset zero index so it prints 1-5
# as opposed to 0-4

# Otherwise variable i will go up to but not include
# the integer passed to range()

# for i in range(5):
#    print('Jimmy Five Times (' + str(i + 1) + ')')

# As a while loop
i = 0

while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i += 1
