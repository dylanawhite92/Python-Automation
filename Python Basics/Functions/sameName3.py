# Modifying global variable using global keyword
# More functions are used to showcase local and global scope

def spam():
    # Modify global variable
    global eggs
    eggs = 'spam'

def bacon():
    # Local variable
    eggs = 'bacon'

def ham():
    # Return global value
    print(eggs)

# Global variable
eggs = 42

# Call function
spam()

# Return value
print(eggs)
