import random

# The "create_board" function creates a board of the given size with all cells initialized to "O" (representing empty sea).
def create_board(board_size, label):
    # create an empty list representing the game board
    board = []
    # iterate over the rows of the board
    for i in range(board_size):
        # create an empty row 
        row = []
        # iterate over the columns of the row 
        for j in range(board_size):
            # add an o to represent sn empty space on the board 
            row.append("O")
            # add the row to the board
        board.append(row)

    # print the label of the board and the current state of the board
    print(f"{label} Board:")
    print_board(board)

    return board

# function to print the current state of the board
def print_board(board):
    # iterate over the rows of the board
    for row in board:
        # join the elements of the row with spaces and print the resulting srting 
        print(" ".join(row))

# Function to randomly place ships on the game board
def place_ships(board, num_ships):
    # iterate over the number of ships to be placed
    ship_row = random.randint(0, len(board) - 1)
    ship_col = random.randint(0, len(board) - 1)
    # place a ship at the selected position
    board[ship_row][ship_col] = "S" 


# function to get guess from user
def get_guess(board_size):
    # loop until a valid guess is entered
    while True:
        # prompt user for a row or column number
        guess_row = input("Guess Row (0-{}): ".format((board_size - 1)))
        guess_col = input("Guess Col (0-{}): ".format((board_size - 1)))

        # if both inputs are digits, convert the to integers
        if guess_row.isdigit() and guess_col.isdigit():
            guess_row = int(guess_row)
            guess_col = int(guess_col)

            # If both inputs are digits, convert them to integers
            if guess_row in range(board_size) and guess_col in range(board_size):
                return guess_row, guess_col


        # if the guess is not valid, print error message and loop again
        print("Invalid guess. Please enter numbers between 0 and {}.".format(board_size - 1))


# function to check if guess hit ship
def check_guess(guess_row, guess_col, board):
    # if guess hit ship, print success message and mark position as hit
    if board[guess_row][guess_col] == "S":
        print("You sunk my ship :'(")
        board[guess_row][guess_col] = "X"
        return True
    # if guess has already been hit, print error message
    elif board[guess_row][guess_col] == "X":
        print("This ship has already sunk...")
    # if the guessed position does not contain a ship, print fail message
    else:
        print("hahaha you missed!")
        board[guess_row][guess_col] = "M"
    return False

# function to check whether the game is over
def is_game_over(board, max_turns):
    # count the number of remaining ships on the board
    num_ships = 0
    for row in board:
        num_ships += row.count("S")
    return num_ships == 0 or max_turns == 0


# main function, start game
def play_game():
    print("Welcome to BattleShip!")
    
    # specify board size
    board_size = int(input("Enter the size of the game board: "))
    computer_board = create_board(board_size, "Computer")

    # specify name displayed on users board
    user_label = input("Enter a label for your board: ")
    user_board = create_board(board_size, user_label)

    num_ships = int(board_size ** 2 * 0.2)

    # place the ships randomly on the computers board
    place_ships(computer_board, num_ships)

    # maximum number of turns for the game
    max_turns = 4

    # loop through each turn
    for turn in range(max_turns):
        print("Turn", turn +1)

        # display the computer's board to user
        print("computer Board:")
        print_board(computer_board)

        # get user's guess
        guess_row, guess_col = get_guess(board_size)

        # check if the users guess hit a ship
        if check_guess(guess_row, guess_col, computer_board):
            break

        # check if game won
        if is_game_over(computer_board, max_turns - turn -1):
            print("Congratulation! You won!")
            break

    # check if game lost
    if not is_game_over(computer_board, max_turns):
        print("GAME OVER, computer wins..")

# function is only executed if the script is being run as the main program
if __name__ == "__main__":
    play_game()