"""
Test 1
October 7, 2014
Author: Rand Seay
Objective: Review all concepts covered in the previous labs
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

"""
Program 1
Objective: Split a five-digit integer and decide which digits are odd and which
are even
"""

def getNumOfLength(lengthOfNum):
    while True:
        userInput = getNumFromUser(
            "int",
            "Please enter a five-digit integer to be split up."
        )

        if len(str(userInput)) == 5:
            break
        else:
            continue

    return userInput

sectionIntro("the five-digit splitter")

userNumber = getNumOfLength(5)

oddNums, evenNums = [], []
for digit in list(str(userNumber)):
    if int(digit) % 2 == 0:
        evenNums.append(digit)
    else:
        oddNums.append(digit)

if len(oddNums) > 0:
    print("\nHere are the odd digits in the number {}:".format(userNumber))
    for number in oddNums:
        print(number, end=" ")
    print()
else:
    print("\nThere are no odd digits in the number {}.".format(userNumber))

if len(evenNums) > 0:
    print("\nHere are the even digits in the number {}:".format(userNumber))
    for number in evenNums:
        print(number, end=" ")
    print()
else:
    print("\nThere are no even digits in the number {}.".format(userNumber))

"""
Program 2
Objective:
"""

"""
Program 3
Objective:
"""

"""
Program 4
Objective:
"""

"""
Program 5
Objective:
"""
