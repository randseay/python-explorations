"""
Author: Rand Seay
Objective: Exam 3
"""

# Part 1
def getData(filename="student_data.txt"):
    """
    Reads in data from a file in the format of 'grade' - 'name'. Returns a
    dictionary of that data.
    """
    studentData = {}
    fileContents = open(filename)
    for line in fileContents:
        studentData[line.split("-")[0].rstrip()] = line.rstrip().split("-")[1].lstrip()
    fileContents.close()
    return studentData

# Part 2
def printDictionary(dictionary, Sorted=False):
    """
    Prints the data in descending order if the 'sorted' argument is 'True' or
    ascending order if there is no 'sorted' argument passed in.
    """
    if not Sorted:
        keyList = sorted(dictionary.keys())
    else:
        keyList = sorted(dictionary.keys(), reverse=True)

    for k in keyList:
        print("{}: {}".format(k, dictionary[k]))

# Part 3
def checkGrades(gradeData):
    """
    Searches the dictionary and returns the name of the students whose grades
    are greater than or equal to 'B'.
    """
    goodGrades = []
    for k, v in gradeData.items():
        if int(v) >= 80:
            goodGrades.append(k)
    return goodGrades

# Part 4
def curveScores(gradeData):
    """
    Calculates and prints the average grade of all students
    """
    gradeTotals = 0
    maxNum = 0
    minNum = 100
    for v in gradeData.values():
        if int(v) > maxNum:
            maxNum = int(v)
        if int(v) < minNum:
            minNum = int(v)
        gradeTotals += int(v)
    return (gradeTotals - maxNum - minNum) / (len(gradeData.items()) - 2)

# Part 5
def numAboveAverage(gradeData):
    """
    Prints the names of all students having a grade above average in ascending
    order of their grade.
    """
    aboveAverage = {}
    for k, v in gradeData.items():
        if int(v) >= curveScores(gradeData):
            aboveAverage[k] = int(v)
    printDictionary(aboveAverage)


def main():
    """
    Document main function
    """
    gradeData = getData()
    print("Ascending Order:")
    printDictionary(gradeData)
    print("\nDescending Order:")
    printDictionary(gradeData, Sorted=True)
    print("\nB or better:\n{}".format(checkGrades(gradeData)))
    print("\nAverage:\n{}".format(curveScores(gradeData)))
    print("\nAbove average:")
    numAboveAverage(gradeData)

main()
