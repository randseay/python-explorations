# Number of cars available
cars = 100

# Number of space in each car
space_in_a_car = 4.0

# Number of drivers available
drivers = 30.0

# Number of passengers who need rides
passengers = 90.0

# Number of cars that will not be driven
cars_not_driven = cars - drivers

# Number of cars that will be driven
cars_driven = drivers

# Number of people able to be transported
carpool_capacity = cars_driven * space_in_a_car

# Number of people per car
average_passengers_per_car = passengers / cars_driven

# Ratio of drivers to passengers
drivers_to_passengers_ratio = drivers / passengers


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

print "Our driver to passenger ratio is %s." % drivers_to_passengers_ratio
print "Hey %s there." % "you"