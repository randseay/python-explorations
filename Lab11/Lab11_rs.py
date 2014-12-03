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
    print("Your hand:\n")
    for card in yourHand:
        print()

def main():
    """
    The main function
    """
    deck = makeDeck()
    yourHand = dealCards(deck)
    print("Here is your hand:\n{}\nvalue: {}".format(yourHand, getHandValue(yourHand)))

    getCard(yourHand, deck)
    print(yourHand)
    print("Here is your hand:\n{}\nvalue: {}".format(yourHand, getHandValue(yourHand)))

    print("The size of the deck is {}.".format(len(deck)))

main()
