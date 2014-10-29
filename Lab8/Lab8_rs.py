"""
Author: Rand Seay
Objective: Write a program that plays hangman
"""

import math, random

images = ("""
   +----+
   |
   |
   |
   |
   |
   |
===========
""","""
   +----+
   |    |
   |
   |
   |
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |
   |
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |    |
   |
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|
   |
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|\\
   |
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|\\
   |   /
   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|\\
   |   /
   |   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|\\
   |   / \\
   |   |
   |
===========
""","""
   +----+
   |    |
   |    O
   |   /|\\
   |   / \\
   |   | |
   |
===========
"""
)
difficulty = (("Easy", 9), ("Medium", 7), ("Hard", 5))
playedWords = []
possibleWords = (
    "tuvw",
    "xyz"
    # "bagpipes",
    # "buffoon",
    # "cobweb",
    # "dwarves",
    # "galvanize",
    # "haphazard",
    # "hyphen",
    # "jigsaw",
    # "keyhole",
    # "microwave",
    # "numbskull",
    # "oxygen",
    # "pneumonia",
    # "rhubarb",
    # "squawk",
    # "vaporize",
    # "whiskey",
    # "zigzag",
    # "zodiak",
    # "zombie",
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

    while True:
        chosenDifficulty = input("\n{}\n> ".format(prompt))

        for level in difficulty:
            if chosenDifficulty.lower() == level[0].lower():
                return level
            else:
                prompt = "Uhh... What? Please try again."
                continue

def getGuess(prompt):
    """
    Retrieves a guess from the user
    """
    while True:
        yourGuess = input("{}\n> ".format(prompt))

        if len(yourGuess) == 1:
            break
        else:
            prompt = "\nWhoops! Please try again."
            continue
    return yourGuess

def checkGuess(secretWord, yourGuess, rightGuesses, wrongGuesses, allGuesses):
    """
    Checks whether a guess is in the targeted word
    """
    if yourGuess not in allGuesses:
        if yourGuess in secretWord:
            print("Nice guess!")
            rightGuesses.append(yourGuess)
        else:
            print("Sorry... wrong!")
            wrongGuesses.append(yourGuess)

    allGuesses.append(yourGuess)

    return rightGuesses, wrongGuesses, allGuesses

def getBoard(numWrong, maxWrong):
    """
    Gets the board based on the number of guesses that are wrong
    """
    if numWrong == 0:
        board = images[0]
    elif numWrong == maxWrong:
        board = images[9]
    else:
        board = images[math.floor((numWrong / maxWrong) * 10)]

    return board

def getProgress(secretWord, rightGuesses):
    """
    Get the progress of the word so far in the game
    """
    resultList = []

    for letter in secretWord:
        resultList.append(letter if letter in rightGuesses else "_")

    result = "".join(resultList) + "\n"

    return result

def executeTurn(secretWord, rightGuesses, wrongGuesses, allGuesses, maxWrong):
    print(getBoard(len(wrongGuesses), maxWrong))
    print(getProgress(secretWord, rightGuesses))
    userGuess = getGuess("What is your guess?")
    checkGuess(secretWord, userGuess, rightGuesses, wrongGuesses, allGuesses)

    return rightGuesses, wrongGuesses, allGuesses

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

def startNewGame(intro):
    """
    Main game function
    """
    print("{}\n".format(intro))

    difficultyLevel, maxWrong = setDifficulty("Which difficulty would you like to play on?")
    secretWord = getNewWord(possibleWords)
    playedWords.append(secretWord)
    rightGuesses = []
    wrongGuesses = []
    allGuesses = []
    youWin = False

    print("\nYour word is selected and you have {} guesses. Good luck... You'll need it!".format(maxWrong))

    while len(wrongGuesses) <= maxWrong:
        executeTurn(secretWord, rightGuesses, wrongGuesses, allGuesses, maxWrong)
        print("Right Guesses:", rightGuesses)
        print("Wrong Guesses:", wrongGuesses)
        print("All Guesses:", allGuesses)

    if youWin:
        print("Congratulations! You guessed the word {} and had {} wrong guesses.".format(secretWord, len(wrongGuesses)))

def main():
    print(images[len(images) - 1])
    startNewGame("="*80 + "\nWelcome to Hangman!\n" + "="*80)


main()
