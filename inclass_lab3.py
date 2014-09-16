"""
Author: Rand Seay
Objective: In-class assignment for the third lab
"""

# Objective: Calculate the discount of an item based on its value.

print("\nWelcome to the discount calculator, where you can find discounts.")
print("="*80)

while True:
    try:
        itemValue = float(input("Please provide a value for an item: "))

        if itemValue > 0:
            break
        else:
            print("That is not a positive value! Please try again.")
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

# Objective: Trucks, Cars, and People

print("\nWelcome to cars, trucks, and people! We can help you get where you are going.")
print("="*80)

while True:
    try:
        trucks = int(input("Trucks hold 5 people. How many trucks are there? "))

        if trucks > 0:
            break
        else:
            print("That is not a positive value! Please try again.")
    except ValueError:
        print("Please provide a real amount of trucks.")

while True:
    try:
        cars = int(input("Cars hold four people. How many cars are there? "))

        if cars > 0:
            break
        else:
            print("That is not a positive value! Please try again.")
    except ValueError:
        print("Please provide a real amount of cars.")

while True:
    try:
        people = int(input("How many people are there? "))

        if people > 0 and people <= 30:
            break
        else:
            print("You can't have that many people! Tell some to go home and try again.")
    except ValueError:
        print("Please provide a real amount of people.")

print("\n{} cars can hold {} people. {} trucks can hold {} people. You have {} people".format(cars, cars*4, trucks, trucks*5, people))

if cars * 4 >= people:
    print("Take cars.")
elif trucks * 5 >= people:
    print("Take trucks.")
else:
    print("It is not possible to get where you want to go with those vehicles. Tough luck.")
