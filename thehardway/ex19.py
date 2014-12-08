# Define function 'cheese_and_crackers' that takes arguments 'cheese_count' and 'boxes_of_crackers'.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Print message and run call 'cheese_and_crackers' with two arguments.
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

# Print message and set variables 'amount_of_cheese' and 'amount_of_crackers'.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Run 'cheese_and_crackers' with new variables 'amount_of_cheese' and 'amount_of_crackers'.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print message and call 'cheese_and_crackers' with math in the arguments.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Print message and run 'cheese_and_crackers' with math in the arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)