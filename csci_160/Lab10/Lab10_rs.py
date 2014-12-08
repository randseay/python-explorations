"""
Author: Rand Seay
Objective: Functions and reuse, problem solving, working with files, lists, and
dictionaries
"""

import math, random

# Assignment 1

def getList(filename):
    """
    Reads in from a file called 'filename' and returns a list of integers.
    """
    fileContents = open(filename)
    scores = []
    for line in fileContents:
        scores.append(int(line))
    return scores

def minValue(scores):
    """
    Returns the minimum value of the list of integers
    """
    lowest = scores[0]
    for score in scores:
        lowest = score if score < lowest else lowest

    return lowest


def maxValue(scores):
    """
    Returns the maximum value of the list of integers
    """
    highest = scores[0]
    for score in scores:
        highest = score if score > highest else highest
    return highest

def rangeOf(scores):
    """
    Returns the range of the list of integers (the difference between the
    largest and smallest values)
    """
    return maxValue(scores) - minValue(scores)

def average(scores):
    """
    Returns the average (or mean) of the list of integers
    """
    return sum(scores) / len(scores)

def stdDev(scores):
    """
    Returns the standard deviation of the list of integers.
    """
    variance = []
    for item in scores:
        variance.append((item - average(scores))**2)
    return math.sqrt(average(variance))

def median(scores):
    """
    Returns the median value of the list of integers
    """
    scores.sort()
    halfIndex = len(scores) // 2
    if len(scores) % 2 == 0:
        return (scores[halfIndex - 1] + scores[halfIndex]) / 2
    else:
        return scores[halfIndex]

def menu():
    """
    Prints out a list of options, line by line. Uses an input to allow the user
    to select an option and returns that selection
    """
    print("="*80 + "\nStatistical Machine\n" + "="*80)
    print("1. Read in file")
    print("2. Compute Maximum")
    print("3. Compute Minimum")
    print("4. Compute Range")
    print("5. Compute Average")
    print("6. Compute Standard Deviation")
    print("7. Compute Median")
    print("8. Exit")
    selection = input("Please select an option\n> ")
    return selection

def main():
    """
    Document's main function
    """
    scores = []
    command = menu()
    while command != "8":
        if command == "1":
            filename = input("Please enter a file name\n> ")
            scores = getList(filename)
            print("File loaded successfully")
        elif command == "2":
            print("The maximum is", maxValue(scores))
        elif command == "3":
            print("The minimum is", minValue(scores))
        elif command == "4":
            print("The range is", rangeOf(scores))
        elif command == "5":
            print("The average is", average(scores))
        elif command == "6":
            print("The standard deviation is", stdDev(scores))
        elif command == "7":
            print("The median is", median(scores))
        command = menu()
    print("Goodbye!\n")

main()

# Assignment 2

def getTeams(filename):
    """
    Reads in a file and returns a list of teams
    """
    fileContents = open(filename)
    teams = {}
    for line in fileContents:
        line = line.rstrip()
        seed = line.split("-")[1]
        teamName = line.split("-")[0]
        teams[int(seed.lstrip())] = teamName.rstrip()
    return teams

def determineWinner(team1, team2):
    """
    Returns the winner between 'team1' and 'team2' based on the random number
    algorithm
    """
    randomNum = random.randint(1,16)
    if team1 < team2:
        if randomNum >= team2:
            return team2
        else:
            return team1
    elif team1 > team2:
        if randomNum >= team1:
            return team1
        else:
            return team2
    else:
        raise Exception("Invalid teams passed to determineWinner.")

def main2():
    """
    Document's second main function
    """
    print("="*80 + "\nMarch Madness Game Picker\n" + "="*80)
    schedule = {
        "game1": [1,16],
        "game2": [2,15],
        "game3": [3,14],
        "game4": [4,13],
        "game5": [5,12],
        "game6": [6,11],
        "game7": [7,10],
        "game8": [8,9],
    }
    teamData = input("Please enter a file name with teams and their seeds\n> ")
    teams = getTeams(teamData)
    print("\nFirst Round Results\n" + "-"*80)
    for k, v in schedule.items():
        print("#{} {} vs. #{} {}".format(v[0], teams[v[0]], v[1], teams[v[1]]))
        print("Winner: {}\n".format(teams[determineWinner(v[0], v[1])]))

main2()
