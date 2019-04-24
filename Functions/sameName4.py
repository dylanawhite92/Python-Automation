# Purposefully producing an error

# Python does not fall back to using global eggs variable in this case
def spam():
    print(eggs)
    eggs = 'spam local'

# Produces error because local variable is referenced before it's assigned
eggs = 'global'
spam()
