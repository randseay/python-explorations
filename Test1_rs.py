"""
Test 1
October 7, 2014
Author: Rand Seay
Objective: Review all concepts covered in the previous labs
"""

from math import pi

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

def getNumOfLength(lengthOfNum, numType="int", prompt=""):
    while True:
        userInput = getNumFromUser(
            numType,
            prompt
        )

        if len(str(userInput)) == lengthOfNum:
            break
        else:
            continue

    return userInput

"""
Program 1
Objective: Split a five-digit integer and decide which digits are odd and which
are even.
"""

sectionIntro("the five-digit splitter")

userNumber = getNumOfLength(5, "int", "Please enter a five digit integer to be split up")

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
Objective: Get the last two digits from a year and return the last two digits as
a string.
"""

sectionIntro("the year splitter.")

userYear = str(getNumOfLength(4, "int", "Please enter a four digit year."))

print("\nThe last two digits of that year is {}.".format(userYear[-2:]))

"""
Program 3
Objective: Find the volume of a sphere and the circumference of a circle.
"""

sectionIntro("the volume of a sphere and circumference of a circle calculator.")

def getVolumeOfSphere(radius):
    return ((4/3) * pi) * radius ** 3

def getCircOfCircle(radius):
    return 2 * pi * radius

userRadiusOfSphere = getNumFromUser(
    "float",
    "Please enter the radius for a sphere to find the volume of.",
    enforcePositiveValue=True
)

userVolumeOfSphere = getVolumeOfSphere(userRadiusOfSphere)

print("\nThe volume of a sphere with a radius of {:.2F} is {:.4F}.\n".format(userRadiusOfSphere, userVolumeOfSphere))

userRadiusOfCircle = getNumFromUser(
    "float",
    "Please enter the radius for a circle to find the circumference of.",
    enforcePositiveValue=True
)

userCircOfCircle = getCircOfCircle(userRadiusOfCircle)

print("\nThe circumference of a circle with a radius of {:.2F} is {:.4F}.\n".format(userRadiusOfCircle, userCircOfCircle))

"""
Program 4
Objective: Get all the even numbers between two values.
"""

"""
Program 5
Objective: Compare any amount of number based on user input, and return the
highest and lowest values.
"""
