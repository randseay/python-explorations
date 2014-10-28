"""
Author: Rand Seay
Objective: Write a program that plays hangman
"""

import random

difficulty = (("Easy", 9), ("Medium", 7), ("Hard", 5))
playedWords = []
possibleWords = (
    "bagpipes",
    "buffoon",
    "cobweb",
    "dwarves",
    "galvanize",
    "haphazard",
    "hyphen",
    "jigsaw",
    "keyhole",
    "microwave",
    "numbskull",
    "oxygen",
    "pneumonia",
    "rhubarb",
    "squawk",
    "vaporize",
    "whiskey",
    "zigzag",
    "zodiak",
    "zombie",
)

def getNewWord(wordList):
    while True:
        result = random.choice(wordList)

        if result in playedWords:
            continue
        else:
            playedWords.append(result)
            break

    return result

def setDifficulty(prompt):
    for level in difficulty:
        print("{:8s}{:2} guesses".format(level[0], level[1]))

    chosenDifficulty = input("\n{}\n> ".format(prompt))

    return chosenDifficulty

def getGuess(prompt):
    """
    Retrieves a guess from the user
    """
    while True:
        yourGuess = input("{}\n> ".format(prompt))

        if len(yourGuess) == 1:
            break
        else:
            prompt = "You may only guess one letter at a time. Please try again."
            continue
    return yourGuess

def checkGuess(targetWord, yourGuess):
    """
    Checks whether a guess is in the targeted word
    """
    if yourGuess in targetWord:
        return True
    else:
        return False

def startNewGame(intro):
    """
    Main game function
    """
    print("{}\n".format(intro))

    selectedDifficulty = setDifficulty("Which difficulty would you like to play on?")

    yourWord = getNewWord(possibleWords)
    print("Your word is selected! Good luck... You'll need it!\n")

    userGuess = getGuess("What is your first guess?")

def playAgain():
    """
    Ask whether or not the user would like to play again
    """
    while True:
        userInput = input("Would you like to play again? (Yy/Nn)\n> ")

        if userInput.lower() == "y":
            return True
        if userInput.lower() == "n":
            return False


# def startGame()

def main():
    startNewGame("="*80 + "\nWelcome to Hangman!\n" + "="*80)


main()
