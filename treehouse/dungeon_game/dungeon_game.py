"""
Title: Dungeon Game
Author: Rand Seay
"""

import random

def make_grid(x, y):
    """
    Creates a grid based on a passed-in width (x) and length (y)
    """
    grid = [(col, row) for col in range(x) for row in range(y)]

    return grid

def get_locations(dungeon):
    """
    Sets random locations for the player, the monster, and the door from a
    passed-in dungeon. If any of them are at the same location, start over.
    """
    # Copy the dungeon
    dungeon_cp = dungeon[:]

    # Shuffle and take the last three coordinates
    random.shuffle(dungeon_cp)
    player = dungeon_cp.pop()
    monster = dungeon_cp.pop()
    door = dungeon_cp.pop()

    return player, monster, door

def print_dungeon(dungeon, player):
    """
    Prints the dungeon and the players position.
    """
    for coord in dungeon:
        print(coord)


def get_moves(player):
    """
    Returns a list of possible moves for the player based on their position
    """
    MOVES = ["LEFT", "RIGHT", "UP", "DOWN"]
    if player[0] == 0:
        MOVES.remove("UP")
    # If player's x is 0, remove UP
    # If player's y is 0, remove LEFT
    # If player's x is max, remove DOWN
    # If player's y is max, remove RIGHT

    return MOVES

def move_player(player, move):
    """
    Gets the player's current location and moves the player, if valid
    """
    # Get the player's position
    # If the move is LEFT, y-1
    # If the move is RIGHT, y+1
    # If the move is UP, x-1
    # If the move is DOWN, x+1

    return player_position

def main():
    """
    The game's main function
    """
    while True:
        print("="*80 + "\nWelcome to the Dungeon Game!\n" + "="*80)

        # Get the dungeon size
        dungeon_width = int(input("How wide would you like the dungeon to be?\n> "))
        dungeon_length = int(input("How long would you like the dungeon to be?\n> "))

        # Set up dungeon and get locations
        dungeon = make_grid(dungeon_width, dungeon_length)
        player, monster, door = get_locations(dungeon)
        print_dungeon(dungeon, player)

        print("You're currently in room {}".format(player))
        print("You can move {}") # Fill in with available moves
        print("Enter QUIT to quit")

        # Get a move
        move = input("> ").upper()
        if move == 'QUIT':
            break

        # If it's a good move, change the player's position
        # If it's a bad move, don't change anything
        # If the new player position is the door, they win!
        # If the new player position is the monster, they lose.
        # Otherwise, continue

main()
