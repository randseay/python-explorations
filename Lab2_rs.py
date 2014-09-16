"""
Author: Rand Seay
Objective: Write various programs that utilizes basic input and output commands,
as well as math and format functions
"""

from math import floor
from datetime import date
from time import strftime

print("="*40)
print("Welcome to Lab2.py... Enjoy!")
print("="*40, "\n")

# Part 1: Always 5
print('This is the game "Always 5", where the answer is always 5!\n')

while True:
    try:
        yourNumber = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("Uh-Oh! That's not going to work, please try again.\n")

print("Magic stuff is happening, please standby...")
print("Multiply by 5: {} * 5 = {}. Add 25: {} + 25 = {}".format(yourNumber, int(yourNumber*5), int(yourNumber*5), int(yourNumber*5+25)))
print("Divide by 5: {} / 5 = {}".format(int(yourNumber*5+25), int((yourNumber*5+25)/5)))
print("Subtract by original number: {} - {} = {}".format(int((yourNumber*5+25)/5), yourNumber, int(((yourNumber*5+25)/5)-yourNumber)))
print("Result: {}".format(int(((yourNumber*5+25)/5)-yourNumber)))
print("Imagine that!")

# Part 2: Dollars and Sense
print("\n", "- "*20, sep="")
print('\nWelcome to the "US Dollar to British Pound Converter", which converts good old US Dollars to British Pounds!\n')
exchangeRate = 0.61

while True:
    try:
        firstAmount = float(input("Please enter a dollar amount: ").strip().lstrip("$").replace(",", ""))
        break
    except ValueError:
        print("That's not a proper dollar amount, please try again.\n")

while True:
    try:
        secondAmount = float(input("I know you have more than that, please enter a second dollar amount: ").strip().lstrip("$").replace(",", ""))
        break
    except ValueError:
        print("That's not a proper dollar amount, please try again.\n")

totalAmount = firstAmount + secondAmount
print("\nSo you really have ${:.2f}.".format(totalAmount))
print("That is the same as {}{:.2f}.".format(u'\u00A3',totalAmount*exchangeRate))

# Part 3: Birthdates: You didn't really thing you were done yet, did you?
print("\n", "- "*20, sep="")
birthDate = int(input("\nPlease enter your month of birth and day as a single number: "))

month = int(floor(birthDate/100))
day = int(birthDate%(month*100))
fullDate = date(2014,month,day)

print("You were born in month {}.".format(month))
print("You were born on day {}.".format(day))
print("Your birthday in 2014 is {:02d}/{:02d}/2014.".format(month,day))

# Challenge: Print out the name of the month instead of the number
print("Another way you could say it is {}.".format(fullDate.strftime("%B %d, %Y")))
print("\n", "- "*20, sep="")

print("\nBye!")
