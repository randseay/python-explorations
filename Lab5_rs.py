"""
Author: Rand Seay
Objective: Working with for loops and writing functions
"""

def sectionIntro(nameOfSection):
    """
    Output a section header based on a passed in name
    """
    print()
    print("="*80)
    print("Welcome to", nameOfSection)
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

# Part 1: Mathematical Calculations

sectionIntro("Mathematical Calculations")

def getNaturalLog(numberOfIterations):
    result, sign = 0, 1

    for num in range(1, numberOfIterations + 1):
        result += sign * (1 / num)
        sign = -sign

    return result

iterationsOfLN = getNumFromUser(
    "int",
    "Please provide a positive whole number to determine the number of iterations\nused in the approximation of natural logarithm.",
    enforcePositiveValue=True
)
print()

print("The natural logarithm after {} iterations is {}".format(iterationsOfLN, getNaturalLog(iterationsOfLN)))

# Part 2: Fibonacci Series

sectionIntro("Fibonacci Series")

def getFibSeries(numberOfIterations):
    fibonacciSeries = []

    for n in range(numberOfIterations):
        if n == 0:
            fibonacciSeries.append(0)
        elif n == 1:
            fibonacciSeries.append(1)
        else:
            fibonacciSeries.append(fibonacciSeries[n - 2] + fibonacciSeries[n - 1])

    return fibonacciSeries

iterationsOfFib = getNumFromUser(
    "int",
    "Please provide a positive whole number to determine the length of the Fibonacci series.",
    enforcePositiveValue=True
)

print("\nHere is your Fibonacci series with a length of {}\n> ".format(iterationsOfFib), end="")
for item in getFibSeries(iterationsOfFib):
    print(item, end=" ")
print()

# Part 3: Count up and count down

sectionIntro("Count up and count down")

def countUp(val1, val2, step=1):
    result = []

    if val1 < val2:
        for value in range(val1, val2 + 1, step):
            result.append(value)
    else:
        for value in range(val2, val1 + 1, step):
            result.append(value)

    return result

def countDown(val1, val2, step=2):
    result = []

    if val1 < val2:
        for value in range(val2, val1 - 1, -step):
            result.append(value)
    else:
        for value in range(val1, val2 - 1, -step):
            result.append(value)

    return result

# Count up

firstUpValue = getNumFromUser("int", "Please provide an initial whole number to count to or from.")
print()
secondUpValue = getNumFromUser("int", "Please provide another whole number to count to or from. The smaller number will be used as a starting number.")
print()
stepUpValue = getNumFromUser(
    "int",
    "Please indicate what the step should be, press ENTER to accept the default of 1.",
    enforcePositiveValue=True,
    specifyDefaultValue=True,
    defaultValue=1
)

print("\nHere is your counting up sequence, counting by {}.".format(stepUpValue))
for item in countUp(firstUpValue, secondUpValue, stepUpValue):
    print(item, end=" ")
print()

# Count Down

print()
firstDownValue = getNumFromUser("int", "Please provide an initial whole number to count down to or down from.")
print()
secondDownValue = getNumFromUser("int", "Please provide another whole number to down to count to or down from. The larger number will be used as a starting number.")
print()
stepDownValue = getNumFromUser(
    "int",
    "Please indicate what the step down should be, press ENTER to accept the default of 2.",
    enforcePositiveValue=True,
    specifyDefaultValue=True,
    defaultValue=2
)

print("\nHere is your counting down sequence, counting by {}.".format(stepDownValue))
for item in countDown(firstDownValue, secondDownValue, stepDownValue):
    print(item, end=" ")
print()

# Part 4: Calculate the calories burned

sectionIntro("Calories Burned")

def caloriesBurned(minutesExercised):
    return 3.4 * minutesExercised

minutesUserExercised = getNumFromUser(
    "float",
    "Please provide the amount of time in minutes that you played Wii Sports.",
    enforcePositiveValue=True
)

print("\nYou played Wii Sports for {:.2F} minutes, and burned {:.2F} calories.".format(minutesUserExercised, caloriesBurned(minutesUserExercised)))
