# Import 'argv' module from 'sys'.
from sys import argv

# Unpack variables 'script' and 'filename' to be taken as arguments.
# script, filename = argv
print "Which file would you like to read? "
filename = raw_input("> ")

# Create variable 'txt' and assign it the file given for 'filename'.
txt = open(filename)

# Print string that includes 'filename' variable.
print "Here's your file %r: " % filename

# Print 'txt' after the file has been read and close it.
print txt.read()
txt.close()

# Print string and assign user input to variable 'file_again'.
print "Type the filename again: "
file_again = raw_input("> ")

# Create variable 'txt_again' and assign it the file given for 'file_again'.
txt_again = open(file_again)

print txt_again.read()
txt_again.close()