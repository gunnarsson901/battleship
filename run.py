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


