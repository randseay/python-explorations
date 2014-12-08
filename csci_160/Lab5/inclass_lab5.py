"""
for letter in 'Python':
    print('Current Letter :', letter)

def addNumbers(num1, num2, num3):
    return num1 + num2 + num3

def main():
    x = 4
    y =5
    z = 10
    return addNumbers(x, y, z)

main()
"""

from random import choice

inventory = {"shoes": 14.50, "pants": 24.12, "shirt": 17.89, "socks": 5.48, "book": 5.51, "hat": 10.88, "coat": 45.15, "Necklace": 89.10}
cart = []

def sectionIntro(nameOfSection):
    """
    Output a section header based on a passed in name
    """
    print()
    print("="*80)
    print("Welcome to", nameOfSection)
    print("="*80)
    print()


def getDollarAmount(prompt):
    """
    Get the dollar amount from the user
    """
    while True:
        try:
            userInput = float(input(prompt + "\n> "))

            if userInput > 0:
                break
            else:
                userInput = "Please provie a positive float value."
        except ValueError:
            userInput = "Please provide a positive float value."
    return userInput

def buyRandomItem(moneyLeft):
    item = choice(list(inventory.keys()))
    cost = inventory[item]
    if cost > 40:
        cost *= .7
    elif cost > 20:
        cost *= .8
    else:
        cost *= .9

    if (moneyLeft - cost) > 0:
        cart.append(item)
        moneyLeft -= cost
    else:
        moneyLeft = -1
    return moneyLeft

# Thanksgiving Shopping

sectionIntro("Holiday Shopping")

money = getDollarAmount("How much money are you bringing shopping?")

while money >= 0:
    moneyRemaining = buyRandomItem(money)

    if moneyRemaining < 0:
        break
    else:
        money = moneyRemaining

print("\nHere is what you decided to buy...")

for item in cart:
    print("{}: {}".format(item, inventory[item]))

print("Now you have ${:.2f} left.".format(money))
