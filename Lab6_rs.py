"""
Author: Rand Seay
Objective: Learn about functions in order to perform various tasks and return
some values
"""

def minimum(firstInt, secondInt):
    return firstInt if firstInt < secondInt else secondInt

def maximum(firstInt, secondInt):
    return firstInt if firstInt > secondInt else secondInt

def isEqual(firstInt, secondInt):
    return True if firstInt == secondInt else False

def isOdd(firstInt):
    return True if firstInt % 2 != 0 else False

def isEven(firstInt):
    return True if firstInt % 2 == 0 else False

def formatDollar(dollarAmount):
    return "${:.2f}".format(dollarAmount)

def letterGrade(labScore):
    letterGrade = "I"

    if labScore < 60:
        letterGrade = "F"
    if labScore < 70:
        letterGrade = "D"
    if labScore < 80:
        letterGrade = "C"
    if labScore < 90:
        letterGrade = "B"
    else:
        letterGrade = "A"

    return letterGrade

def exponent(firstValue, secondValue):
    return firstValue ** secondValue

def makeCoolUserName(chosenUserName, symbol, repeatAmount):
    return symbol * repeatAmount + chosenUserName + symbol * repeatAmount

def greeting(nameToGreet, age):
    return "Hello, {}! Your age is {}.".format(nameToGreet, age)

def main():
    int1 = 15 #int(input("Give me an int: "))
    int2 = 17 #int(input("Give me another int: "))
    val1 = 5 #int(input("Give me a value: "))
    val2 = 4 #int(input("Give me another value: "))
    amount = 55.88076651 #float(input("Give me a float: "))
    labScore = 81 #int(input("Give me a lab score (0-100): "))
    userName = "swagMaster" #input("Give me a username: ")
    name = "Voldemort" #input("Give me your name: ")
    print("minimum:",minimum(int1, int2))
    print("maximum:",maximum(int1, int2))
    print("isEqual:",isEqual(int1, int2))
    print("isOdd:",isOdd(int1))
    print("isEven:",isEven(int1))
    print("formatDollar:",formatDollar(amount))
    print("letterGrade:",letterGrade(labScore))
    print("exponent:",exponent(val1,val2))
    print("makeCoolUserName:",makeCoolUserName(userName,"$",5))
    print("greeting:",greeting(name,int2))

main()
