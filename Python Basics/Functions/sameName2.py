# Modifying global variable using global keyword

def spam():
    global eggs
    eggs = 'spam'

# Eggs variable is originally set to global
eggs = 'global'

# Calling spam() function modifies global variable
spam()

# Return value
print(eggs)
