"""
Author: Rand Seay
Objective: Working with Dictionaries (assignment 1) and files (assignment 2)
"""

# Assignment 1

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
            print("Improperly formatted data in line {} ({})".format(lineNum, line.strip()))
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
    print("The GPA: {:.2F}".format(getGPA(classes)))

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
    if className in classes:
        classes[className] = grade
        return True
    else:
        return False

def takenClass(classes, className):
    """
    Returns True if the class is in the dictionary and False if it is not
    """
    return True if className in classes else False

def printAllGrades(classes):
    """
    Prints all the grades (separated by spaces)
    """
    print("All Grades:")
    for k, v in classes.items():
        print(v, end = " ")
    print()

def numberOfGrades(classes):
    """
    Returns a new dictionary with the letter grades as keys and number of
    instances of that grade as a value
    """
    gradeAccumulator = {}
    for k, v in classes.items():
        if v in gradeAccumulator:
            gradeAccumulator[v] += 1
        else:
            gradeAccumulator[v] = 1

    return gradeAccumulator

def printClassesWithHigherGrade(classes, grade):
    """
    Prints all the classes (in the same format as printClasses) where the grade
    for the class is equal to or greater then the grade passed in
    """
    sortedKeys = list(classes.keys())
    sortedKeys.sort()
    sortedClasses = {}
    count = 0
    for key in sortedKeys:
        if classes[key] <= grade:
            count += 1
            print("{}. {:8s}: {}".format(count, key, classes[key]))
            sortedClasses[key] = classes[key]
    print("The GPA: {:.2F}".format(getGPA(sortedClasses)))

def main():
    """
    The main function
    """
    # Initialize classes dictionary
    classes = {}

    # Add a class
    addClass(classes, "ENGR 220", "A")

    # Import report card
    importReportCard(classes)

    # Drop a class
    dropClass(classes, "MATH 370")

    # Print classes
    printClasses(classes)
    print("-"*80)

    # Edit grade
    editGrade(classes, "CSci 160", "B")

    # Check if student has taken a class
    print("Student has taken CSci 160:", takenClass(classes, "CSci 160"))
    print("Student has taken CHEM 330:", takenClass(classes, "CHEM 330"))
    print("-"*80)

    # Print All Grades
    printAllGrades(classes)
    print("-"*80)

    # Print number of grades
    print("Number of grades:\n{}".format(numberOfGrades(classes)))
    print("-"*80)

    # Print classes with a higher grade
    gradeToSort = "B"
    print("Classes with a {} or higher:".format(gradeToSort))
    printClassesWithHigherGrade(classes, gradeToSort)

main()

# Assignment 2

def main2():
    # Step 1
    file1 = open("file1.txt", "r")
    file2 = open("file2.txt", "r")

    # Step 2
    file3 = open("file3.txt", "w")
    file3.write(file1.read())
    file3.write(file2.read())

    # Cleanup
    file1.close()
    file2.close()
    file3.close()

    # Step 3
    dataFile = open("file3.txt", "r")
    file4 = open("file4.txt", "w")
    wordCount = 0
    for line in dataFile:
        wordList = line.rstrip().split(" ")
        wordList.sort()
        for word in wordList:
            file4.write(word + "\n")

            # Step 4
            if word.strip("--").strip("*").strip(".").strip(",").strip("!").replace("'","").isalpha():
                wordCount += 1
    print("-"*80)
    print("There are {} words in file4.txt".format(wordCount))

    # Cleanup
    file4.close()

main2()
