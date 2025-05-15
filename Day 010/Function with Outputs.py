# Function with input parameters and output
def format_name(f_name, l_name):
    fullname = f"{f_name.title()} {l_name.title()}"
    return fullname

my_Name = format_name("chris", "harley")
print(my_Name)

# Using a function within a function
def echo(text):
    echo_text = f"{text}....{text}..........{text}........."
    return echo_text

my_Echo = echo(format_name("noVa", "StePH"))
print(my_Echo)
