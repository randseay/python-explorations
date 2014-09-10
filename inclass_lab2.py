"""
Author: Rand Seay
Objective: Calculate the GPA of two students based on their grades in three courses
"""

studentName = input("Please enter the first student's name: ")
numberOfClasses = 3
gradeValues = {"a": 4, "b": 3, "c": 2, "d": 1}
studentGrades = {}

for x in range(numberOfClasses):
    studentClass = input("Please enter a class name: ").lower()
    studentGrade = input("Please enter the letter grade: ").lower()
    studentGrades[studentClass] = studentGrade

gradeTotal = 0

for key in studentGrades:
    gradeTotal += gradeValues[studentGrades[key]]

print("{}'s GPA is {}.".format(studentName, gradeTotal/numberOfClasses, ".2f"))
