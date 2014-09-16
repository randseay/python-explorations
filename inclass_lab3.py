"""
Author: Rand Seay
Objective: Calculate the discount of an item based on its value.
"""

while True:
    try:
        itemValue = float(input("Please provide a value for an item: "))
        break
    except ValueError:
        print("That is not a valid value! Please try again.")

if itemValue >= 10 and itemValue < 20:
    discount = .1
elif itemValue >= 20 and itemValue < 30:
    discount = .2
elif itemValue >= 30 and itemValue < 40:
    discount = .3
else:
    discount = -1

if discount != -1:
    print("Your discount is {:.0%}!".format(discount))
else:
    print("There is currently no discount for an item of that value. Sorry.")
