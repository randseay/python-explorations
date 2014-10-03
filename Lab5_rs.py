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

def getNumFromUser(valueType, prompt, positiveValue=False, defaultValue=False):
    """
    Return a numeric value based on passed-in type and prompt
    """
    while True:
        try:
            if valueType == "integer" or valueType == "int":
                userInput = int(input(prompt + "\n> "))
                if userInput == "":
                    if defaultValue:
                        userInput = int(defaultValue)
                    else:
                        raise RuntimeError("Default value is invalid ({}).".format(defaultValue))
            elif valueType == "float":
                userInput = float(input(prompt + "\n> "))
                if userInput == "":
                    if defaultValue:
                        userInput = float(defaultValue)
                    else:
                        raise RuntimeError("Default value is invalid ({}).".format(defaultValue))
            else:
                raise RuntimeError("Invalid valueType parameter, please select 'int' (or 'integer') or 'float'.")

            if positiveValue:
                if userInput > 0:
                    break
                else:
                    print("Number was specified as positive, but is not positive ({}).\n".format(userInput))
            else:
                break
        except:
            raise RuntimeError("Invalid data type passed to getNumFromUser under the set conditions ({}).".format(valueType))
    return userInput

def getIntFromUser(prompt):
    """
    Return an integer based on user input and a passed-in prompt
    """
    while True:
        try:
            userInput = int(input(prompt + "\n> "))
        except ValueError:
            userInput = "Please provide a positive whole number as a value"

        break
    return userInput

def getPositiveIntFromUser(prompt):
    """
    Return a positive integer based on user input and a passed-in prompt
    """
    while True:
        try:
            userInput = int(input(prompt + "\n> "))

            if userInput > 0:
                break
            else:
                userInput = "Please provide a positive whole number as a value."
        except ValueError:
            userInput = "Please provide a positive whole number as a value"
    return userInput

def requestPositiveIntFromUser(prompt, default):
    """
    Optionally return a positive integer based on user input and a passed-in prompt
    """
    userInput = int(default)
    while True:
        try:
            userInput = int(input(prompt + "\n> "))

            if userInput > 0:
                break
            else:
                userInput = "Please provide a positive whole number as a value."
        except ValueError:
            userInput = "Please provide a positive whole number as a value"
    return userInput

# getNumFromUser Test
testNumber = getNumFromUser("int", "Please choose a positive integer.", positiveValue=True, defaultValue=2)
print("Your test number is {}.".format(testNumber))

# Part 1: Mathematical Calculations

sectionIntro("Mathematical Calculations")

def getNaturalLog(numberOfIterations):
    result, sign = 0, 1

    for num in range(1, numberOfIterations + 1):
        result += sign * (1 / num)
        sign = -sign

    return result

iterationsOfLN = getPositiveIntFromUser("Please provide a positive whole number to determine the number of iterations\nused in the approximation of natural logarithm.")
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

iterationsOfFib = getPositiveIntFromUser("Please provide a positive whole number to determine the length of the Fibonacci series.")

print("\nHere is your Fibonacci series with a length of {}\n> ".format(iterationsOfFib), end="")
for item in getFibSeries(iterationsOfFib):
    print(item, end=" ")
print()

# Part 3: Count up and count down

sectionIntro("Count up and count down")

def countUp(val1, val2, step=1):
    result = []

    if val1 < val2:
        for value in range(val1, val2, step):
            result.append(value)
    else:
        for value in range(val2, val1, step):
            result.append(value)

    return result

def countDown(val1, val2, step=1):
    result = []

    return result

firstValue = getIntFromUser("Please provide an initial value to count to or from.")
secondValue = getIntFromUser("Please provide another value to count to or from. The smaller number will be used as a starting number.")
stepValue = requestPositiveIntFromUser("Please indicate what the step should be, press enter to accept the default of 1.", 1)

countUp(firstValue, secondValue, stepValue)


# Part 4: Calculate the calories burned



# Part 5: Draw a Triangle


