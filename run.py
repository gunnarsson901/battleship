#The "create_board" function creates a board of the given size with all cells initialized to "O" (representing empty sea).
def create_board(board_size, label):
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append("O")
        board.append(row)