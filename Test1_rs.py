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

sectionIntro("the even number finder.")

userFirstValue = getNumFromUser(
    "int",
    "Please provide an initial value to set an upper or lower bound on the set of even numbers."
)

print()
userSecondValue = getNumFromUser(
    "int",
    "Please provide another value to set an upper or lower bound on the set of even numbers."
)

listOfEvenNums = []
if userFirstValue < userSecondValue:
    for num in range(userFirstValue, userSecondValue + 1):
        if num % 2 == 0:
            listOfEvenNums.append(num)
else:
    for num in range(userSecondValue, userFirstValue - 1):
        if num % 2 == 0:
            listOfEvenNums.append(num)

if len(listOfEvenNums) > 0:
    print("\nThe even numbers between those two values are: ", end="")
    for item in listOfEvenNums:
        print(item, end=",")
    print()
else:
    print("\nThere are no even numbers between the values {} and {}.".format(userFirstValue, userSecondValue))

"""
Program 5
Objective: Compare any amount of number based on user input, and return the
highest and lowest values.
"""

sectionIntro("the maximum and minimum calculator.")

userNumsToCompare = getNumFromUser(
    "int",
    "Please enter how many numbers you would like to compare when finding the maximum and the minimum.",
    enforcePositiveValue=True
)

listToMaxMin = []
for num in range(1, userNumsToCompare + 1):
    print()
    numFromUser = getNumFromUser(
        "float",
        "Number " + str(num),
    )
    listToMaxMin.append(numFromUser)

print("\nThe lowest number is {} and the highest number is {}.".format(min(listToMaxMin), max(listToMaxMin)))
