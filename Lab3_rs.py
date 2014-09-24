"""
Author: Rand Seay
Objective: Work with "If" statements, basic input/output commands, math
functions, and the format function
"""

from math import pi
from re import match

# Part 1: What I need is just the area!

print("="*80)
print("Welcome to the area calculator, which calculates the area of shapes.")
print("="*80)

shapeList = ["circle", "square", "triangle"]

def areaOfCircle(radius):
    "Calculate the area of a circle based on the length of the radius"
    return pi * radius ** 2

def areaOfSquare(side):
    "Calculate the area of a square based on the length of the side"
    return side ** 2

def areaOfTriangle(base, height):
    "Calculate the area of a triangle based on the lengths of the base and height"
    return 0.5 * base * height

while True:
    try:
        selectedShape = int(input("Please pick one: \n\n1. Circle\n2. Square\n3. Triangle\n4. Exit\n> "))

        if selectedShape == 1:
            while True:
                try:
                    circleRadius = float(input("Please provide a radius for the circle: "))

                    if circleRadius > 0:
                        break
                    else:
                        print("A negative number cannot be used as a radius.")
                except ValueError:
                    print("That is not a valid radius, please try again.")

            area = areaOfCircle(circleRadius)
            break

        elif selectedShape == 2:
            while True:
                try:
                    sideLength = float(input("Please provide the side length for the square: "))

                    if sideLength > 0:
                        break
                    else:
                        print("A negative number cannot be used as a side length.")
                except ValueError:
                    print("That is not a valid side length, please try again.")

            area = areaOfSquare(sideLength)
            break

        elif selectedShape == 3:
            while True:
                try:
                    baseLength = float(input("Please provide the base length for the triangle: "))

                    if baseLength > 0:
                        break
                    else:
                        print("A negative number cannot be used as a base length.")
                except ValueError:
                    print("That is not a valid base length, please try again.")

            while True:
                try:
                    heightLength = float(input("Please provide the height for the triangle: "))

                    if heightLength > 0:
                        break
                    else:
                        print("A negative number cannot be used as a base length.")
                except ValueError:
                    print("That is not a valid height, please try again.")
            area = areaOfTriangle(baseLength, heightLength)
            break
        elif selectedShape == 4:
            break
        else:
            print("Please enter either circle, square, or triangle.")
    except ValueError:
        print("Invalid input. Try again and make sure you use a number for the option you would like.")

if selectedShape == 4:
    print("Exiting without calculating an area... Goodbye!")
else:
    print("\nThe area of your {} is {:.2f}".format(shapeList[int(selectedShape)-1], area))

# Part 2: Addition of all digits

print()
print("="*80)
print("Welcome to digit addition machine. It can find the sum of a five digit number")
print("="*80)

while True:
    try:
        yourNumber = int(input("Please enter a five-digit whole number (Ranging from 10000-99999): "))

        if yourNumber > 9999 and yourNumber < 100000:
            break
        else:
            print("Please enter a valid five-digit number")
    except ValueError:
        print("Please enter a valid five-digit number")

yourSum = sum(map(int, str(yourNumber)))

print("The sum of the digits in {} is {}.".format(yourNumber,yourSum))

# Part 3: ASCII values!

print()
print("="*80)
print("Welcome to the ASCII value finder. It finds the ASCII value for a particular letter")
print("="*80)

while True:
    try:
        yourLetter = str(input("Please enter a letter (A-Z): "))

        if match("^[a-zA-Z]*$", yourLetter) and len(yourLetter) == 1:
            break
        else:
            print("Please enter a valid letter in the english aphabet (A-Z)")
    except ValueError:
        print("Please enter a valid letter in the english alphabet (A-Z)")

asciiValue = ord(yourLetter)

print("ASCII value: {}".format(asciiValue))

# Part 4: Final result

print()
print("="*80)
print("Welcome to the final result, which provides the product of all the previous answers")
print("="*80)

finalResult = area * yourSum * asciiValue

print("Result = {:.2f} * {} * {} = {:.2f}".format(area, yourSum, asciiValue, finalResult))

if finalResult > 50001:
    print("Large values")
elif finalResult > 5001:
    print("Medium values")
elif finalResult >= 0:
    print("Small values")
else:
    print("The number cannot be described.")
