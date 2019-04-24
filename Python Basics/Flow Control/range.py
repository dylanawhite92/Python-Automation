# Practice with utilizing range() in for loops

# import random module
import random

# Starting at integer other than zero
for i in range(12, 16):
    print(i)

# Include step argument to iterate in intervals of two
for i in range(0, 10, 2):
    print(i)

# Decrement loop from 5 to 0
for i in range(5, -1, -1):
    print(i)

# Generate random integers between 1 and 10 at each step
for i in range(5):
    print(random.randint(1, 10))
