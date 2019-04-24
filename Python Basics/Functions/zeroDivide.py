# Define function for simple division
# Introduce exception handling
def spam(divisor):
    try:
        return 42 / divisor
    except ZeroDivisionError:
        print('Error: BBZZRRT. Invalid argument.')

print(spam(2))
print(spam(12))
# Throws ZeroDivisionError and fails to continue without exception handling
print(spam(0))
print(spam(1))
