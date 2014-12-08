"""
Author: Rand Seay
Objective: Learn About Functions
"""

def sectionIntro(nameOfSection):
    """
    Output a section header based on a passed in name
    """
    print()
    print("="*80)
    print("Welcome to {}.".format(nameOfSection))
    print("="*80)
    print()

def getNumFromUser(valueType, prompt, enforcePositiveValue=False, specifyDefaultValue=False, defaultValue=0):
    """
    Return a numeric value based on passed-in type and prompt
    """
    while True:
        try:
            if valueType == "integer" or valueType == "int":

                userInput = input(prompt + "\n> ")

                if defaultValue and userInput == "":
                    try:
                        userInput = int(defaultValue)
                    except ValueError:
                        raise RuntimeError("The specified default value ({}) is invalid.".format(defaultValue))
                else:
                    try:
                        userInput = int(userInput)
                    except (ValueError, TypeError) as e:
                        print("Unable to cast value ({}) as an integer. Please try again.\n".format(userInput))
                        continue

            if valueType == "float":

                userInput = input(prompt + "\n> ")

                if defaultValue and userInput == "":
                    try:
                        userInput = float(defaultValue)
                    except ValueError:
                        raise RuntimeError("The specified default value ({}) is invalid.".format(defaultValue))
                else:
                    try:
                        userInput = float(userInput)
                    except (ValueError, TypeError) as e:
                        print("Unable to cast value ({}) as a float. Please try again.\n".format(userInput))
                        continue

            if enforcePositiveValue:
                if userInput > 0:
                    break
                else:
                    print("Number was specified as positive, but is not positive ({}). Please try again.\n".format(userInput))
            else:
                break
        except:
            raise RuntimeError("Invalid data type passed to getNumFromUser under the set conditions ({}).".format(valueType))
    return userInput

def calculateCars(amountOfPeople):
    """
    Calculate how many cars are needed to move a certain amount of people.
    """
    result = 0

    if amountOfPeople % 4 == 0:
        result = amountOfPeople / 4
    else:
        result = (amountOfPeople // 4) + 1


    return result

possibleLocations = ["macy's", "jcpenney"]

def getShoppingLocation(prompt):
    while True:
        try:
            userInput = str(input(prompt + "\n> "))

            if userInput.lower() in possibleLocations:
                break
            else:
                print("Not in the list of possible locations. Please enter either 'Macy's or 'JCPenney'.")
                continue
        except ValueError:
            print("Please enter either 'Macy's' or 'JCPenney'.")

    return userInput

def getDiscount(shoppingLocation, itemPrice):
    discount = 0

    if shoppingLocation.lower() == "macy's":
        if itemPrice <= 15:
            discount = .05
        elif itemPrice <= 30:
            discount = .1
        else:
            discount = .15
    elif shoppingLocation.lower() == "jcpenney":
        if itemPrice <= 20:
            discount = .1
        elif itemPrice <= 30:
            discount = .2
        else:
            discount = .3
    else:
        raise Exception("{} is not a valid shopping location.".format(shoppingLocation))

    return discount


def main():
    sectionIntro("Travel Calculator")

    people = getNumFromUser(
        "int",
        "How many people do you need to move?",
        enforcePositiveValue=True
    )

    print("\nIn order to transport {} people, you need {} cars.".format(people, int(calculateCars(people))))

    sectionIntro("Shopping Trip")

    dollarAmount = getNumFromUser(
        "float",
        "How much money are you bringng with you shopping?",
        enforcePositiveValue=True
    )

    chosenLocation = getShoppingLocation("Where would you like to go shopping?")

    chosenItemPrice = getNumFromUser(
        "float",
        "What is the cost of the item you would like to purchase?",
        enforcePositiveValue=True
    )

    itemDiscount = getDiscount(chosenLocation, chosenItemPrice)
    discountedPrice = chosenItemPrice - (chosenItemPrice * itemDiscount)

    print("While shopping at {}, an item that costs {:.2f} has a discount of {:.2%}, meaning it will cost {:.2f}.".format(chosenLocation, chosenItemPrice, itemDiscount, discountedPrice))

    if dollarAmount >= discountedPrice:
        print("Now that you have bought it, you have {:.2f} left.".format(dollarAmount - discountedPrice))
    else:
        print("You can't afford that!")

main()
