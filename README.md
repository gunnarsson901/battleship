# Battleship Game

This is a simple implementation of the classic Battleship game in Python. The game is played between the user and the computer. The user enters the size of the game board and places their ships on the board. The computer also places its ships randomly on the board. The game then starts and the user and computer take turns guessing the location of the other's ships. The first player to sink all of the other's ships wins the game.

## Usage

To play the game, simply run the `battleship.py` file in your Python environment:


The game will then prompt you to enter the size of the game board and the label for your board. You will then be prompted to place your ships on the board. After you have placed your ships, the computer will randomly place its ships. The game will then start and you will be prompted to guess the location of the computer's ships. The computer will also guess the location of your ships. The game continues until one player has sunk all of the other's ships.

## Implementation

The game is implemented using Python 3. The `battleship.py` file contains all the code necessary to run the game. The code is divided into several functions:

- `create_board`: Creates a new game board of the given size with all cells initialized to "O" (representing empty sea).
- `print_board`: Prints the current state of the game board to the console.
- `place_ships`: Places a specified number of ships randomly on the game board.
- `get_guess`: Prompts the user to enter a row and column number for their guess and returns the guess as a tuple.
- `check_guess`: Checks whether the user's guess hit a ship and updates the game board accordingly.
- `is_game_over`: Checks whether the game is over (i.e., whether all ships have been sunk or the maximum number of turns has been reached).

The main function `play_game` is responsible for running the game. It prompts the user for the size of the game board and the label for their board, creates the user's board and the computer's board, places the computer's ships, and then enters a loop where the user and the computer take turns guessing the location of each other's ships. The loop continues until one player has sunk all of the other's ships or the maximum number of turns has been reached.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
