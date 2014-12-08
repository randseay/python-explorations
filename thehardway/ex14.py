# Import 'argv' module from 'sys'.
from sys import argv

# Unpack variables 'script' and 'user_name' from 'argv' module.
script, user_name, what_time = argv

# Create 'ask' variable and assign it a string value.
ask = '> '

# Begin asking questions using variables. User response assigns to variable 'likes'.
print "Hi %s, I'm the %s script. It is %s" % (user_name, script, what_time)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(ask)

# Ask additional question. User input assigns to variable 'lives'.
print "Where do you live %s?" % user_name
lives = raw_input(ask)

# Ask additional question. User input assigns to variable 'computer'.
print "What kind of computer do you have?"
computer = raw_input(ask)

# Print summary using variables assigned by user input.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)