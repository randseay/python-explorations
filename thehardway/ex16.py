# Import argument variable from 'sys' module.
from sys import argv

# Unpack argument variable and assign it to script' and 'filename'. 
script, filename = argv

# Print intro and instructions, referencing 'filename' variable.
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#  Request user input in order to proceed.
raw_input("?")

# Print message and assign the opened 'filename' (whose mode is 'write') to the contents of 'target'.
print "Opening the file..."
target = open(filename, 'w')

# Truncate the 'target' variable.
print "Truncating the file... Goodbye!"
target.truncate()

# Print message
print "Now I'm going to ask you for three lines."

# Assign user input to the variables 'line1', 'line2', and 'line3'.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# Print message
print "I'm going to write these to the file."

# Write 'line1', 'line2', and 'line3' to the contents of 'target'.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Print closing message and close the file.
print "And finally, we close it."
target.close()