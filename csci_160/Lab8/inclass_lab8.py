aList = list(range(1,10))

def getInput(functionToAsk):
    """
    Ask whether or not the user would like to complete a module
    """
    while True:
        userInput = input("Would you like to {}? (Yy/Nn)\n> ".format(functionToAsk))

        if userInput.lower() == "y":
            return True
        if userInput.lower() == "n":
            return False

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

def main():
    if getInput("append"):
        aList.append(getNumFromUser(
                "int",
                "What value would you like to append to the list?",
                enforcePositiveValue=True
            )
        )
    print("Your list:\n>", aList)

    if getInput("insert"):
        aList.insert(getNumFromUser(
                "int",
                "At what postion would you like to insert a value?",
                enforcePositiveValue=True
            ),
            getNumFromUser(
                "int",
                "What value would you like to insert there?",
                enforcePositiveValue=True
            )
        )
    print("Your list:\n>", aList)

    if getInput("remove"):
        aList.remove(getNumFromUser(
                "int",
                "At what postion would you like to remove a value?",
                enforcePositiveValue=True
            )
        )
    print("Your list:\n>", aList)

    if getInput("pop"):
        print("Popped value:", aList.pop(getNumFromUser(
                "int",
                "At what postion would you like to pop a value?",
                enforcePositiveValue=True
            )
        ))
    print("Your list:\n>", aList)

    if getInput("index"):
        print("Index:", aList.index(getNumFromUser(
                "int",
                "Which value would you like to find the index of?",
                enforcePositiveValue=True
            )
        ))
    print("Your list:\n>", aList)

    if getInput("sort"):
        aList.sort()
    print("Your list:\n>", aList)

    if getInput("reverse"):
        aList.reverse()
    print("Your list:\n>", aList)

main()
