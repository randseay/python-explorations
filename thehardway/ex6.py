# Create variable 'x' and assign it a string value.
x = "There are %d types of people." % 10

# Create variable 'binary' and assign it a string value
binary = "binary"

# Create variable 'do_not' and assign it a string value
do_not = "don't"

# Create variable 'y' and assign it a string value
y = "Those who know %s and those who %s." % (binary, do_not)

# Print variables 'x' and 'y'
print x
print y

# Print strings that reference variables 'x' and 'y'
print "I said: %r." % x
print "I also said: '%s'." % y

# Create variable 'hilarious' and assign it a boolean value
hilarious = False

# Create variable 'joke_evaluation' and assign it a string value
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the evaluation of the variable 'joke_evaluation' with the 'hilarious' variable used within it.
print joke_evaluation % hilarious

# Create variable 'w' and assign it a string value
w = "This is the left side of..."

# Create variable 'e' and assign it a string value
e = "a string with a right side."

# Evaluate the addition of variables 'w' and 'e'
print w + e