name = 'Zed A. Shaw'
age = 35.00 # not a lie
height = 74.00 # inches
weight = 180.00 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
centis = height * 2.54
kilos = weight * 0.453592

print "Let's talk about %s." % name
print "He's %d centimeters tall." % centis
print "He's %d kilograms heavy." % kilos
print "Actually he's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)