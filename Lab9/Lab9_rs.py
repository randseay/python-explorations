"""
Author: Rand Seay
Objective: Working with Dictionaries
"""

def addClass(classes, className, grade):
    """
    Adds a class with className to the classes dictionary and return True if it
    was added or False if it is already in the dictionary
    """
    if className in classes:
        return False
    else:
        classes[className] = grade
        return True

def importReportCard(classes, filename="reportcard.txt"):
    """
    Reads in a file containing class names and grades, which are separated by a
    ':' (colon), then the contents of the report card are added to the classes
    dictionary
    """
    inputFile = open(filename)
    lineNum = 1
    for line in inputFile:
        if ":" in line:
            splitLine = line.strip().split(":")
            addClass(classes, splitLine[0], splitLine[1])
        else:
            print("Improperly formatted line data in line {} ({})".format(lineNum, line.strip()))
        lineNum += 1
    return(classes)


def dropClass(classes, className):
    """
    Drops (removes) a class with className from the classes dictionary and
    returns True if it was removed or False if it was not in the dictionary
    """
    if className in classes:
        del classes[className]
        return True
    else:
        return False

def printClasses(classes):
    """
    Prints out all of the classes, with the GPA at the end
    """
    sortedKeys = list(classes.keys())
    sortedKeys.sort()
    count = 0
    for key in sortedKeys:
        count += 1
        print("{}. {:8s}: {}".format(count, key, classes[key]))
    print("The GPA: {}".format(getGPA(classes)))

def getGPA(classes):
    """
    Returns the GPA for the classes passed in as a floating point number
    """
    GPA = 0.00
    gradeTotal = 0
    for k, v in classes.items():
        if v.lower() == 'a':
            gradeTotal += 4
        elif v.lower() == 'b':
            gradeTotal += 3
        elif v.lower() == 'c':
            gradeTotal += 2
        elif v.lower() == 'd':
            gradeTotal += 1
        elif v.lower() == 'f':
            gradeTotal += 0
        else:
            print("Invalid letter grade ({})".format(v))

    GPA = gradeTotal / len(classes)
    return GPA

def editGrade(classes, className, grade):
    """
    Edits the grade of a certain class and returns True if it was successful
    and false if the class is not in the dictionary
    """

def takenClass(classes, className):
    """
    Returns True if the class is in the dictionary and False if it is not
    """

def printAllGrades(classes):
    """
    Prints all the grades (separated by spaces)
    """

def numberOfGrades(classes):
    """
    Returns a new dictionary with the letter grades as keys and number of
    instances of that grade as a value
    """

def printClassesWithHigherGrade(classes,grade):
    """
    Prints all the classes (in the same format as printClasses) where the grade
    for the class is equal to or greater then the grade passed in
    """

def main():
    """
    The main function
    """

    classes = {}

    importReportCard(classes)
    printClasses(classes)

main()
