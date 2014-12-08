"""
Author: Rand Seay
Objective: Math, I/O, Looping, Problem Solving
"""

def getBA(fileName="bats.txt"):
    """
    Calculate a player's Batting Average (BA)
    """

    fileContents = open(fileName, "r")
    hits = 0
    atBats = 0
    BA = 0
    playerNumber = fileContents.readline().rstrip()

    for line in fileContents:
        plateAppearance = line.rstrip()

        if int(plateAppearance) > 0:
            hits += 1
        atBats += 1

    BA = hits / atBats

    fileContents.close()
    return playerNumber, BA

def getAvgBases(fileName="bats.txt"):
    """
    Calculate the number of bases a player reached
    """

    fileContents = open(fileName, "r")
    basesReached = 0
    atBats = 0
    avgBases = 0
    playerNumber = fileContents.readline().rstrip()

    for line in fileContents:
        plateAppearance = line.rstrip()

        if abs(int(plateAppearance)) > 0:
            basesReached += abs(int(plateAppearance))
        atBats += 1

    avgBases = basesReached / atBats

    fileContents.close()
    return playerNumber, avgBases

def main():
    playerNumber, battingAVG = getBA()
    # Find the Batting Average
    print("The batting average for player #{} is {:.3f}.".format(playerNumber, battingAVG))

    # Find the On Base Percentage
    playerNumber, avgBases = getAvgBases()
    print("The average bases for player #{} is {:.3f}.".format(playerNumber, avgBases))

main()
