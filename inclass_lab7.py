"""
Author: Rand Seay
Objective: Learn about files
"""

from math import ceil

file = open("testdata.txt", "r+")
firstName = "Rand"

file.write("This is a test\n")
file.write("My name is {:s}\n".format(firstName))
file.write("And here is another line\n")

file.close()

def countApples(filename="fruit.txt"):
    fileContents = open(filename, "r") #read file contents
    numApples = 0
    for line in fileContents: #loop through file, line by line
        fruit = line.rstrip() #we get the newline regardless! Get rid of it
        if (fruit.lower() == "apple"):
            numApples += 1
    fileContents.close()
    return numApples

def countFruit(filename="fruit.txt"):
    fileContents = open('fruit.txt')
    numLines = sum(1 for line in fileContents)
    fileContents.close()
    return numLines

def main():
    numApples = countApples()
    numFruit = countFruit()

    print("The number of apples is {}.".format(countApples()))
    print("The number of fruits is {}.".format(countFruit()))
    print("With a capacity of four fruits per car, {} cars are needed to transport {} fruits".format(ceil(numFruit / 4), numFruit))

main()
