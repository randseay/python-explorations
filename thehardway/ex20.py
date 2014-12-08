# Import 'argv' (argument variable) from 'sys' module.
from sys import argv

# Unpack 'script' and 'input_file' from 'argv'.
script, input_file = argv

# Define 'print_all' function and pass it an argument of 'f'.
def print_all(f):

    # Call 'read' on 'f' and print out the result.
    print f.read()

# Define 'rewind' function, and pass it an argument of 'f'.
def rewind(f):

    # Call 'seek' on 'f' and pass in the argument of '0'.
    f.seek(0)

# Define 'print_a_line' function and pass it the arguments 'line_count' and 'f'.
def print_a_line(line_count, f):

    # Print 'line_count' and the result of calling 'readline' on 'f'.
    print line_count, f.readline()

# Call 'open' on 'input_file' and assign it to the variable 'current_file'.
current_file = open(input_file)

# Print string.
print "First let's print the whole file:\n"

# Call 'print_all' on 'current_file'.
print_all(current_file)

# Print string.
print "Now let's rewind, kind of like a tape."

# call 'rewind' on 'current_file'.
rewind(current_file)

# Print string.
print "Let's print three lines:"

# Define 'current_line' as 1.
current_line= 1

# Call 'print_a_line' with the arguments 'current_line' (1) and 'current_file'.
print_a_line(current_line, current_file)

# Define 'current_line' as 'current_line' (1) + 1.
current_line += 1

# Call 'print_a_line' with arguments 'current_line' (2) and 'current_file'.
print_a_line(current_line, current_file)

# Define 'current_line' as 'current_line' (2) + 1.
current_line += 1

# Call 'print_a_line' with arguments 'current_line' (2) + 1.
print_a_line(current_line, current_file)