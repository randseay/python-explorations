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
    for line in inputFile:
        if ":" in line:
            splitLine = line.strip().split(":")
            addClass(classes, splitLine[0], splitLine[1])
        else:
            print("Improperly formatt line {}".format(line.strip()))
    return(classes)


def dropClass(classes, className):
    """
    Drops (removes) a class with className from the classes dictionary and
    returns True if it was removed or False if it was not in the dictionary
    """

def printClasses(classes):
    """
    Prints out all of the classes
    """

def getGPA(classes):
    """
    Returns the GPA for the classes passed in as a floating point number
    """

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

    print(classes)



main()
