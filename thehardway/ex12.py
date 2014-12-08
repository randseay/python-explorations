# Create variable and assign them raw_input values with prompts for the user
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

# Print string with all of the variables
print "So, you're %r old, %r tall, and %r heavy." % (age, height, weight)