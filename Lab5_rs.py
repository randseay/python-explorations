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

def getIntFromUser(prompt):
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

# Part 1: Mathematical Calculations

sectionIntro("Mathematical Calculations")

def getNaturalLog(numberOfIterations):
    result, sign = 0, 1

    for num in range(1, numberOfIterations + 1):
        result += sign * (1 / num)
        sign = -sign

    return result

iterationsOfLN = getIntFromUser("Please provide a positive whole number to determine the number of iterations\nused in the approximation of natural logarithm.")
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

iterationsOfFib = getIntFromUser("Please provide a positive whole number to determine the length of the Fibonacci series.")

print("\nHere is your Fibonacci series with a length of {}\n> ".format(iterationsOfFib), end="")
for item in getFibSeries(iterationsOfFib):
    print(item, end=" ")
print()

# Part 3: Count up and count down



# Part 4: Calculate the calories burned



# Part 5: Draw a Triangle


