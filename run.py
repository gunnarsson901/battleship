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