# Print strings and request user input for age variables
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "What is your favorite color?"
color = raw_input()
print "What is your favorite food?"
food = raw_input()

# Print summary string
print "So, you are %r old, %r tall and %r heavy." % (age, height, weight)
print "I can't believe your favorite color is %r" % color
print "and that your favorite food is %r!" % food