""" Battleship Game
This script implements a terminal-based version of the classic Battleship game.
Allows players to configure the board size, place ships manually, and compete
against a computer opponent. The game uses NumPy for board management and Rich
for colorful terminal output.
"""
import random
import numpy as np
from rich.console import Console
from rich.table import Table

# Constants for symbols
EMPTY_CELL = '~'
HIT_CELL = 'X'
MISS_CELL = 'O'

# Configure Rich console for output
console = Console()

# Possible ship types and their length, based on board size
POSSIBLE_SHIPS = {
    5: {'S': 1, 'D': 2, 'C': 3},  # 5x5: 2-3 ships, length 1-3
    8: {'S': 2, 'D': 3, 'C': 4},  # 8x8: 3-4 ships, length 2-4
    10: {'S': 2, 'D': 3, 'C': 4, 'B': 5},  # 10x10: 4-5 ships, length 2-5
    12: {'S': 2, 'D': 3, 'C': 4, 'B': 5}  # 12x12: 5-7 ships, length 2-5
}

# Player have to choose a gameboard size.
def get_board_size():
    """
    Prompt the user to select a board size for the game.

    Returns:
        int: The chosen board size, wich must be one of the predefined sizes (5, 8, 10, 12).
    """
    while True:
        try:
            size = int(input("Select the board size (5, 8, 10 or 12): \n"))
            if size in POSSIBLE_SHIPS:
                return size
            else:
                print("Enter a valid choice: 5, 8, 10, or 12.")
        except ValueError:
            print("Invalid input! Enter a number between 5 and 12.")

# Player choose amont of ships to the boardsize player have chosen.
def choose_ships(size):
    """
    Allow the player to choose the number of ships based on the selected board size.

    Args:
        size (int): The size of the board.

    Returns:
        dict: A dictionary of ship types and their lengths.
    """
    max_ships = {5: (2, 3), 8: (3, 4), 10: (4, 5), 12: (5, 7)}
    min_ships, max_ships = max_ships[size]
    while True:
        try:
            prompt = f"Select the number of ships (between {min_ships} and {max_ships}): \n"
            num_ships = int(input(prompt))
            if min_ships <= num_ships <= max_ships:
                return dict(list(POSSIBLE_SHIPS[size].items())[:num_ships])

            print(f"Enter a number between {min_ships} and {max_ships}.")
        except ValueError:
            print("Invalid input! Enter an integer.")

# The creation av the board
def create_board(size):
    """
    Create a new game board filled with empty cells.

    Args:
        size (int): The size of the board (number of rows and columns).

    Returns:
        numpy.ndarray: The initialized game board.
    """
    # Create a NumPy board with EMPTY_CELL as the default
    return np.full((size, size), EMPTY_CELL)

# The board will be displayed to the screen
def display_board(board, reveal=False):
    """
    Display the game board using Rich for better visualization.

    Args:
        board (numpy.ndarray): The game board to display.
        reveal (bool): Whether to reveal hidden ships on the board.
    """
    size = board.shape[0]
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column(" ")
    for i in range(size):
        table.add_column(str(i))

    for row_idx, row in enumerate(board):
        row_cells = []
        for cell in row:
            if cell == HIT_CELL:
                cell_display = "[red]X[/red]"
            elif cell == MISS_CELL:
                cell_display = "[blue]O[/blue]"
            else:
                cell_display = EMPTY_CELL

            row_cells.append(
                f"[green]{cell}[/green]" if reveal and cell in ['S', 'D', 'C', 'B']
                    else cell_display
            )
        table.add_row(str(row_idx), *row_cells)

    console.print(table)

def is_position_valid(board, row, col, length, direction):
    """
    Check if a ship can be placed starting at a specific position on the board.

    Args:
        board (numpy.ndarray): The game board.
        row (int): The starting row.
        col (int): The starting column.
        length (int): The length of the ship.
        direction (str): The direction ('h' for horizontal, 'v' for vertical).

    Returns:
        bool: True if the position is valid, False otherwise.
    """
    size = board.shape[0]
    if direction == 'h':
        if col + length > size:
            return False
        return all(board[row, col + i] == EMPTY_CELL for i in range(length))
    elif direction == 'v':
        if row + length > size:
            return False
        return all(board[row + i, col] == EMPTY_CELL for i in range(length))
    return False

def place_ship_on_board(board, row, col, length, direction, ship_type):
    """
    Place a ship on the board at a specific position.

    Args:
        board (numpy.ndarray): The game board.
        row (int): The starting row.
        col (int): The starting column.
        length (int): The length of the ship.
        direction (str): The direction ('h' for horizontal, 'v' for vertical).
        ship_type (str): The type of the ship (e.g., 'S', 'D').
    """
    if direction == 'h':
        for i in range(length):
            board[row, col + i] = ship_type
    elif direction == 'v':
        for i in range(length):
            board[row + i, col] = ship_type

# Code for placing ships: allows the player to select positions for their ships,
def place_ship_manually(board, ship_type, length):
    """
    Allow the player to place a ship manually on the board.

    Args:
        board (numpy.ndarray): The game board.
        ship_type (str): The type of the ship (e.g., 'S', 'D').
        length (int): The length of the ship.
    """
    size = board.shape[0]
    print(f"\nPlace the ship '{ship_type}' which is {length} squares long.")
    placed = False
    while not placed:
        try:
            # Input start position
            user_input = input("Enter the starting position for the ship (row column): \n")
            row, col = map(int, user_input.split())

            # Check if the start position is within bounds
            if row < 0 or row >= size or col < 0 or col >= size:
                print("The starting position is out of bounds. Try again.")
                continue

            # Input direction
            direction = input("Enter direction (h for horizontal, v for vertical): \n").lower()

            if direction not in ['h', 'v']:
                print("Invalid direction. Use 'h' for horizontal or 'v' for vertical. Try again.")
                continue
            if is_position_valid(board, row, col, length, direction):
                place_ship_on_board(board, row, col, length, direction, ship_type)
                placed = True
            else:
                print("The ship doesn't fit or the position is occupied. Try again.")
        except (ValueError, IndexError):
            print("Incorrect input! Ensure you enter valid numbers and try again.")

# and the program will place them accordingly.
def place_all_ships_manually(board, ships):
    """
    Allow the player to place all their ships manually on the board.

    Args:
        board (numpy.ndarray): The player's game board.
        ships (dict): A dictionary of ship types and their lengths.
    """
    for ship, length in ships.items():
        display_board(board, reveal=True)
        place_ship_manually(board, ship, length)

# Code for placing the computers ships,
def place_ship_computer(board, length):
    """
    Randomly place a ship of a given length on the board.

    Args:
        board (numpy.ndarray): The game board where the ship will be placed.
        length (int): The length of the ship to be placed.
    """
    size = board.shape[0]
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row, col = random.randint(0, size - 1), random.randint(0, size - length)
            if all(board[row, col + i] == EMPTY_CELL for i in range(length)):
                for i in range(length):
                    board[row, col + i] = 'S'
                placed = True
        else:
            row, col = random.randint(0, size - length), random.randint(0, size - 1)
            if all(board[row + i, col] == EMPTY_CELL for i in range(length)):
                for i in range(length):
                    board[row + i, col] = 'S'
                placed = True

# and the program will place the computers ships.
def place_all_ships_computer(board, ships):
    """
    Randomly place all ships for the computer.

    Args:
        board (numpy.ndarray): The computer's game board.
        ships (dict): A dictionary of ship types and their lengths.
    """
    for _, length in ships.items():
        place_ship_computer(board, length)

# Code that handles the player's turn to choose a target
def player_turn(board):
    """
    Allow the player to take a turn by targeting a cell on the opponent's board.

    Args:
        board (numpy.ndarray): The opponent's game board.

    Returns:
        bool: True if the player hits a ship, False otherwise.
    """
    print("\nYour turn! Use the format row column (e.g., 2 3)")
    try:
        row, col = map(int, input("Enter row and column: \n").split())
        if board[row, col] in POSSIBLE_SHIPS[5].keys():
            board[row, col] = HIT_CELL
            print("Hit!")
            return True
        if board[row, col] == EMPTY_CELL:
            board[row, col] = MISS_CELL
            print("Miss!")
            return False
        print("Already used! Try again.")
        return player_turn(board)
    except (ValueError, IndexError):
        print("Invalid input! Try again.")
        return player_turn(board)

# Code that handles the computer's turn to choose a target.
def computer_turn(board):
    """
    Allow the computer to take a turn by targeting a cell on the player's board.

    Args:
        board (numpy.ndarray): The player's game board.

    Returns:
        bool: True if the computer hits a ship, False otherwise.
    """
    size = board.shape[0]
    row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    while board[row, col] in [HIT_CELL, MISS_CELL]:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    if board[row, col] in POSSIBLE_SHIPS[5].keys():
        board[row, col] = HIT_CELL
        print(f"The computer hit at {row} {col}!")
        return True
    board[row, col] = MISS_CELL
    print(f"The computer missed at {row} {col}.")
    return False

# Function to check if all ships have been hit, indicating a win.
# Returns True if no cells with ships remain on the board.
def check_win(board, ships):
    """
    Check if all ships on a board have been sunk.

    Args:
        board (numpy.ndarray): The game board.
        ships (dict): A dictionary of ship types and their lengths.

    Returns:
        bool: True if all ships have been sunk, False otherwise.
    """
    return all(cell not in ships.keys() for row in board for cell in row)

# Main function to start the Battleship game.
# Greets the player, sets the board size, and creates the player and computer boards.
def main():
    """
    Main function to run the Battleship game.
    """
    print("Welcome to Battleship!")
    board_size = get_board_size()
    player_board = create_board(board_size)
    computer_board = create_board(board_size)

    # Selects the ships based on the chosen board size.
    selected_ships = choose_ships(board_size)

    # Places all ships manually on the player's board and automatically on the computer's board.
    place_all_ships_manually(player_board, selected_ships)
    place_all_ships_computer(computer_board, selected_ships)

    # Enters a loop to display both the player's board and the computer's board.
    # Player's board is shown with all ships revealed, while the computer's board hides the ships.
    while True:
        print("\nYour board:")
        display_board(player_board, reveal=True)
        print("\nComputer's board:")
        display_board(computer_board)

        # Checks if the player's turn results in a hit on the computer's board.
        # If the player has hit all of the computer's ships, message is displayed, the game ends.
        if player_turn(computer_board):
            if check_win(computer_board, selected_ships):
                print("Congratulations! You have defeated the computer!")
                break

        # Checks if the computer's turn results in a hit on the player's board.
        # If the computer has hit all of the player's ships, message is displayed, the game ends.
        if computer_turn(player_board):
            if check_win(player_board, selected_ships):
                print("The computer won! Better luck next time!")
                break

# Checks if the script is being run directly and, if so, starts the main function.
if __name__ == "__main__":
    main()
