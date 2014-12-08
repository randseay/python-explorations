# IMPORT

from random import randint

# DEFINE FUNCTIONS

def make_board():
    columns = int(raw_input("How many columns would you like in the game board? "))
    rows = int(raw_input("\nHow many rows would you like in the game board? "))
    board = []
    for each_item in range(0,columns):
        board.append(["O"] * columns)

    def print_board(rows):
        for each_item in range(0,rows):
            print " ".join(board[each_item])

    print "\n-------------------------------------------------------------------------------"      
    print "Here is your game board. You probably could have made it more difficult, weeny."
    print "-------------------------------------------------------------------------------\n"

    print_board(rows);

    def random_col(board):
        return randint(0,columns - 1)

    def random_row(board):
        return randint(0,rows - 1)

    ship_col = random_col(board)
    ship_row = random_row(board)

    print "\n---------------------------------------"
    print "ALERT! There is an enemy ship in range!"
    print "---------------------------------------\n"
    print "Anticipate its coordinates and annihilate it!\n"

    def check_guess():
        guess_col = int(raw_input("     Guess Col > "))
        guess_row = int(raw_input("     Guess Row > "))
        if ship_row == guess_row and ship_col == guess_col:
            print "\n++++++++++++++++++++++++++++++++++++++++"
            print "Congratulations! You sank my battleship!"
            print "++++++++++++++++++++++++++++++++++++++++\n"
            again = raw_input("     Would you like to play again? ")
            if again.lower().slice(0,1) == "y":
                make_board();
            else:
                print "Until next time loser!"
        else:
            elif guess_row < 0 or guess_row > rows - 1 or guess_col < 0 or guess_col > columns - 1:
                print "\n---------------------------------------------"
                print "You blockhead, you didn't even hit the ocean!"
                print "---------------------------------------------\n"
                print_board(rows);
                print "\n------------"
                print "Keep firing!"
                print "------------\n"
                check_guess();
            elif board[guess_col][guess_row] == "X":
                print "\n------------------------------------"
                print "You already guessed that you nimwit!"
                print "------------------------------------\n"
                print_board(rows);
                print "\n------------"
                print "Keep firing!"
                print "------------\n"
                check_guess();
            else:
                print "\n----------------------------------------------------"
                print "Negative impact. Try to suck less next time. Sheesh."
                print "----------------------------------------------------\n"
                board[int(guess_col)][int(guess_row)] = "X"
                print_board(rows);
                print "\n---------------------------"
                print "Hurry up bozo! Keep firing!"
                print "---------------------------\n"
                check_guess();

    check_guess();

# BEGIN GAME

print """
                                     |\/
                                     ---                
                                     / | [
Welcome to Battleship!        !      | |||
                            _/|     _/|-++'
                        +  +--|    |--|--|_ |-     Made by Rand Seay
                     { /|__|  |/\__|  |--- |||__/          
                    +---------------___[}-_===_.'____                 /\
                ____`-' ||___-{]_| _[}-  |     |_[___\==--            \/   _
 __..._____--==/___]_|__|_____________________________[___\==--____,------' .7
|                                                                     BB-61/
 \_________________________________________________________________________|
 Art by Matthew Bace
 """

make_board();