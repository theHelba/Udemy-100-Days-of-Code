programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Print an item in a dictionary
print(programming_dictionary["Bug"])


# Add pair to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)


# Create an empty dictionary
empty_dictionary = {}


# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)


# Loop through a dictionary
for i in programming_dictionary:
    print(i) # Prints keys
    print(programming_dictionary[i]) # Prints values


# Wipe existing dictionary
programming_dictionary = {}
print(programming_dictionary)
