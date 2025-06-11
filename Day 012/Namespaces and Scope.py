# Global Scope
# Variables or functions declared at the top level 
# (unindented) of a code file have global scope. 
# It is accessible anywhere in the code file.
enemies = 1

# Local Scope
# Variables (or functions) declared inside functions have 
# local scope (also called function scope). They are only 
# seen by other code within the same block of code.
def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}") # Prints 1
