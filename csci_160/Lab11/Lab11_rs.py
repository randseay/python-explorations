"""
Author: Rand Seay
Objective: Work with dictionaries and lists, and be an awesome gambler.
"""
import random

# Blackjack Program

faceCardValues = {
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 11
}

def makeDeck():
    """
    Creates a new deck of cards
    """
    suits = ["spades", "hearts", "clubs", "diamonds"]
    num = list(range(2,11))
    num.extend(['jack','queen','king','ace'])
    return [(j,i) for j in num for i in suits]

def dealCards(deck):
    """
    Deals cards from a passed in deck and returns a hand of cards
    """
    hand = []
    random.shuffle(deck)
    hand.append(deck.pop())
    hand.append(deck.pop())
    return hand

def getHandValue(hand):
    """
    Calculates and returns the value of a passed in hand of cards
    """
    value = 0
    numOfAces = 0
    for card in hand:
        if card[0] in faceCardValues:
            value += int(faceCardValues[card[0]])
            if card[0] == "ace":
                numOfAces += 1
        else:
            value += int(card[0])

    for card in range(1, numOfAces + 1):
        if value > 21:
            value -= 10
    return value

def getCard(hand, deck):
    """
    Gets a card from a passed in deck of cards, and adds it to the passed in
    hand of cards
    """
    hand.append(deck.pop())
    return hand, deck

def printHand(hand):
    """
    Prints a passed in hand of cards
    """
    print("\nYour hand:")
    for card in hand:
        print("\t{cardValue} of {cardSuit}".format(cardValue=card[0],cardSuit=card[1]))
    print("Value: {}\n".format(getHandValue(hand)))

def playAgain(playing):
    while True:
        keepPlaying = input("\nWould you like to play again? (y/n)\n> ")

        if keepPlaying.lower() == "y":
            return True
        elif keepPlaying.lower() == "n":
            return False
        else:
            print("Please try again.\n")


def main():
    """
    The main function
    """
    print("="*40 + "\nWelcome to Blackjack!\n" + "="*40)
    playing = True
    while playing:
        deck = makeDeck()
        print("-"*40)
        yourHand = dealCards(deck)
        printHand(yourHand)

        while True:
            userInput = (input("Would you like to hit or stand?\n> "))
            if userInput == "hit":
                getCard(yourHand, deck)
                printHand(yourHand)
                if getHandValue(yourHand) > 21:
                    print("Bust! You lose!")
                    break
            elif userInput == "stand":
                break
            else:
                print("Please try again.\n")

        if getHandValue(yourHand) == 21:
            print("Nice! You win with 21!")
        elif getHandValue(yourHand) > 17 and getHandValue(yourHand) < 21:
            print("Good job, you win with {}".format(getHandValue(yourHand)))
        elif getHandValue(yourHand) <= 17:
            print("Sorry, {} wasn't good enough to win".format(getHandValue(yourHand)))

        if not playAgain(playing):
            print("\nGoodbye!")
            playing = False

main()
