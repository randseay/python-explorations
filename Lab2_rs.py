"""
Author: Rand Seay
Objective: Write various programs that utilizes basic input and output commands,
as well as math and format functions
"""

# Part 1: Always 5
# print('Welcome to the game "Always 5", where the answer is always 5!\n')

# while True:
#     try:
#         yourNumber = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Uh-Oh! Looks like that isn't a number, please try again.\n")

# print("Magic stuff is happening, please standby...")
# print("Your number is... {}! Imagine that!".format(int(((yourNumber*5+25)/5)-yourNumber)))

# Part 2: Dollars and Sense
print('Welcome to the "US Dollar to British Pound Converter", which converts good old US Dollars to British Pounds!\n')

while True:
    try:
        firstAmount = float(input("Please enter a dollar amount: ").strip().lstrip("$").replace(",", ""))
        secondAmount = float(input("I know you have more than that, please enter a second dollar amount: ").strip().lstrip("$").replace(",", ""))
        break
    except ValueError:
        print("That's not a proper dollar amount, please try again.\n")

print("Your dollar amount is", firstAmount + secondAmount)

# Part 3: You didn't really thing you were done yet, did you?

# Challenge
