# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print()

greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is like in {location}?")
    print()

# Positional Argument
greet_with("Chris", "Arkansas")

# Keyword Argument
greet_with(location="Arkansas", name="Chris")