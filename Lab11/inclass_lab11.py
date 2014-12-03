"""
Author: Rand Seay
Objective: Work with dictionaries
"""

# Part 1

def main():
    wordFile = open("words.txt")
    wordList = []
    filteredList = []

    for line in wordFile:
        wordList.append(line.rstrip())
    wordFile.close()

    firstLetter = input("Type the first letter you would like to filter (r). Type 'QUIT' to exit.\n> ")
    if firstLetter != "QUIT":
        for word in wordList:
            if word[0] == firstLetter:
                filteredList.append(word)

    print(filteredList)

    secondLetter = input("Type the second letter you would like to filter. 'QUIT' to exit.\n> ")
    if secondLetter != "QUIT":
        for word in filteredList:
            if word[1] != secondLetter:
                filteredList.remove(word)

    print(filteredList)

    # Part 2

    codexFile = open("keys.txt")
    codex = {}

    for line in codexFile:
        codex[line.rstrip()] = ""
    codexFile.close()

    keyCount = 0
    for key in codex.keys():
        codex[key] = wordList[keyCount]
        keyCount += 1

    print(codex)

    fileToEncrypt = open("original.txt")
    linesToEncrypt = []

    for line in fileToEncrypt:
        linesToEncrypt.append(line.rstrip())
    fileToEncrypt.close()

    print(linesToEncrypt)

main()
