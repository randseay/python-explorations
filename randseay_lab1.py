"""
Write a program that uses variables to store your first name,
last name, Course ID, Course Name, Name of School, and email address.
"""

firstName = "Rand"
lastName = "Seay"
courseID = "CSci 160"
courseName = "Computer Science I"
email = "rand.seay@ndus.edu"
schoolName = "University of North Dakota"

# Using three print statements
print(firstName,lastName)
print(courseID,courseName,email)
print(schoolName)

# Using one print statement
print("{} {}\n{} {} {}\n{}".format(firstName,lastName,courseID,courseName,email,schoolName))

# Using six print statements
print(firstName, end=" ")
print(lastName)
print(courseID, end=" ")
print(courseName, end=" ")
print(email)
print(schoolName)
