# Import 'argv' from 'sys' module and 'exists' from 'os.path' module.
from sys import argv
from os.path import exists

# Unpack 'script', 'from_file', and 'to_file' from 'argv'.
script, from_file, to_file, = argv

# Print message to user explaining which files will be copied to and from.
print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line too, how?
# Create 'in_file' and 'indata' and assign them to open 'from_file' and to read the opened 'from_file'.
# These two can be placed on one line with the use of a semicolon.
indata = open(from_file).read()

# Print the length of 'indata'
print "The input file is %d bytes long" % len(indata)

# Print message and determine whether or not the output file exists.
print "Does the output file exist? %r" % exists(to_file)

# Reqest whether the user would like to proceed.
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# Assign to 'out_file' the opened 'to_file' in write mode. Write 'indata' to the 'out_file'
out_file = open(to_file, 'w')
out_file.write(indata)

# Print closing message.
print "Alright, all done."

# Close both 'out_file' and 'in_file'.
out_file.close()