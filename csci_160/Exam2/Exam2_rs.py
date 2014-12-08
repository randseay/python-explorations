"""
Author: Rand Seay
Objective: Exam 2
"""

# Part 1

def fillList1(filename):
    """
    This function takes a filename, parses the numbers into a list, and returns
    the list filled with the values
    """
    inFile = open(filename)
    listOfValues = []
    for line in inFile:
        listOfValues.append(line.strip())
    return listOfValues


def fillList2(filename):
    """
    This function takes in a filename, parses the names of the students into a
    list, and returns the list filled with the values
    """
    inFile = open(filename)
    listOfValues = []
    for line in inFile:
        listOfValues.append(line.strip())
    return listOfValues

# Part 2

def printList1(numbers, Sorted=False):
    """
    This function prints out the values in numbers, line by line. However, it
    only writes out the values between 0 and 9 (inclusive). It prints out the
    numbers sorted in descending order if "Sorted" value is "True" (default is
    "False".)
    """
    numberList = numbers[:]
    if Sorted:
        numberList.sort()
    for item in numberList:
        if float(item) >= 0 and float(item) <= 9:
            print(item)

def printList2(names, Sorted=False):
    """
    This function prints out the values in names, line by line. It prints out
    the names sorted in descending order if "Sorted" value is "True" (default
    is "False".)
    """
    nameList = names[:]
    if Sorted:
        nameList.sort()
    for item in nameList:
        print(item)

# Part 3

def studentMatches(names, searchVal):
    """
    This function searches the list of students and returns the number of times
    "searchVal" occurs in the list.
    """
    result = 0
    for item in names:
        if item == searchVal:
            result += 1
    return result

# Part 4

def curveScores(numbers):
    """
    This function calculates and returns the average of numbers as a float,
    ignoring both the largest and the smallest values (if there are two maximum
    values, then only one of them is ignored). It does not modify the original
    list.
    """
    average = 0
    allScores = 0
    highScore = 0
    lowScore = 0
    for item in numbers:
        if float(item) < lowScore:
            lowScore = float(item)
        if float(item) > highScore:
            highScore = float(item)
        allScores += float(item)
    average = (allScores - highScore - lowScore) / (len(numbers) - 2)
    return average

# Part 5

def numAboveAverage(numbers):
    """
    This functions determines the number of values in numbers that are above
    average and returns this value as an integer. It uses the actual average,
    not the curved version.
    """
    aboveAverageCount = 0
    averageScore = sum([float(i) for i in numbers]) / len(numbers)
    for item in numbers:
        if float(item) > averageScore:
            aboveAverageCount += 1
    return aboveAverageCount

def main():
    """
    The main function
    """
    numbers = fillList1("scores.txt")
    names = fillList2("students.txt")
    printList1(numbers)
    printList1(numbers, True)
    printList2(names)
    printList2(names, True)
    print("Number of times Tom is in the list:", studentMatches(names, "Tom"))
    print("Number of times AB is in the list:", studentMatches(names, "AB"))
    print("Number of times Madhu is in the list:", studentMatches(names, "Madhu"))
    print("Curved Average:", curveScores(numbers))
    print("Number of Values above average in the list:", numAboveAverage(numbers))

main()
