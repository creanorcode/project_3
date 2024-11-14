# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

EMPTY_CELL = '~'
HIT_CELL = 'X'
MISS_CELL = 'O'

#Possible ship types and their length
POSSIBLE_SHIPS = {
    5: {'S': 1, 'D': 2, 'C': 3}, # 5x5: 2-3 ships, length 1-3
    8: {'S': 2, 'D': 3, 'C': 4}, # 8x8: 3-4 ships, length 2-4
    10: {'S': 2, 'D': 3, 'C': 4, 'B': 5}, # 10x10: 4-5 ships, length 2-5
    12: {'S': 2, 'D': 3, 'C': 4, 'B': 5} # 12x12: 5-7 ships, length 2-5
}

# Player have to choose a gameboard size.
def get_board_size():
    while True:
        try:
            size = int(input("Select the board size (5, 8, 10 or 12): "))
            if size in POSSIBLE_SHIPS:
                return size
            else:
                print("Enter a valid choice: 5, 8, 10, or 12.")
        except ValueError:
            print("Invalid input! Enter a number between 5 and 12.")

# Player choose amont of ships to the boardsize player have chosen.
def choose_ships(size):
    max_ships = {5: (2, 3), 8: (3, 4), 10: (4, 5), 12: (5, 7)}
    min_ships, max_ships = max_ships[size]
    while True:
        try:
            num_ships = int(input(f"Select the number of ships (between {min_ships} and {max_ships}): "))
            if min_ships <= num_ships <= max_ships:
                return dict(list(POSSIBLE_SHIPS[size].items())[:num_ships])
            else:
                print(f"Enter a number between {min_ships} and {max_ships}.")
        except ValueError:
            print("Invalid input! Enter an integer.")

# The creation av the board
def create_board(size):
    return [[EMPTY_CELL for _ in range(size)] for _ in range(size)]

# The board will be printed to the screen
def print_board(board, reveal=False):
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            row_display.append(cell if reveal or cell in [HIT_CELL, MISS_CELL] else EMPTY_CELL)
        print(f"{i} " + " ".join(row_display))

# Code for placing ships: allows the player to select positions for their ships,
def place_ship_manually(board, ship_type, length):
    size = len(board)
    print(f"\nPlace the ship '{ship_type}' which is {length} squares long.")
    placed = False
    while not placed:
        try:
            row, col = map(int, input("Enter the starting position for the ship (row column): ").split())
            direction = input("Enter direction (h for horizontal, v for vertical): ").lower()
            if direction == 'h' and col + length <= size:
                if all(board[row][col + i] == EMPTY_CELL for i in range(length)):
                    for i in range(length):
                        board[row][col + i] = ship_type
                    placed = True
                else:
                    print("The location is already occupied. Try again.")
            elif direction == 'v' and row + length <= size:
                if all(board[row + i][col] == EMPTY_CELL for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = ship_type
                    placed = True
                else:
                    print("The location is already occupied. Try again.")
            else:
                print("Invalid position or direction. Try again.")
        except (ValueError, IndexError):
            print("Incorrect input! Try again.")

# and the program will place them accordingly.
def place_all_ships_manually(board, ships):
    for ship, length in ships.items():
        print_board(board, reveal=True)
        place_ship_manually(board, ship, length)

# Code for placing the computers ships,
def place_ship_computer(board, length):
    size = len(board)
    placed = False
    while not placed:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row, col = random.randint(0, size - 1), random.randint(0, size - length)
            if all(board[row][col + i] == EMPTY_CELL for i in range(length)):
                for i in range(length):
                    board[row][col + i] = 'S'
                placed = True
        else:
            row, col = random.randint(0, size - length), random.randint(0, size - 1)
            if all(board[row + i][col] == EMPTY_CELL for i in range(length)):
                for i in range(length):
                    board[row + i][col] = 'S'
                placed = True

# and the program will place the computers ships.
def place_all_ships_computer(board, ships):
    for ship, length in ships.items():
        place_ship_computer(board, length)

# Code that handles the player's turn to choose a target
def player_turn(board):
    print("\nYour turn! Use the format row column (e.g., 2 3)")
    try:
        row, col = map(int, input("Enter row and column: ").split())
        if board[row][col] in POSSIBLE_SHIPS[5].keys():
            board[row][col] = HIT_CELL
            print("Hit!")
            return True
        elif board[row][col] == EMPTY_CELL:
            board[row][col] = MISS_CELL
            print("Miss!")
            return False
        else:
            print("Already used! Try again.")
            return player_turn(board)
    except (ValueError, IndexError):
        print("Invalid input! Try again.")
        return player_turn(board)

# Code that handles the computer's turn to choose a target.
def computer_turn(board):
    size = len(board)
    row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    while board[row][col] in [HIT_CELL, MISS_CELL]:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    if board[row][col] in POSSIBLE_SHIPS[5].keys():
        board[row][col] = HIT_CELL
        print(f"The computer hit at {row} {col}!")
        return True
    else:
        board[row][col] = MISS_CELL
        print(f"The computer missed at {row} {col}.")
        return False

# Function to check if all ships have been hit, indicating a win.
# Returns True if no cells with ships remain on the board.
def check_win(board, ships):
    return all(cell not in ships.keys() for row in board for cell in row)

# Main function to start the Battleship game.
# Greets the player, sets the board size, and creates the player and computer boards.
def main():
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
    # The player's board is shown with all ships revealed, while the computer's board hides the ships.
    while True:
        print("\nYour board:")
        print_board(player_board, reveal=True)
        print("\nComputer's board:")
        print_board(computer_board)

        # Checks if the player's turn results in a hit on the computer's board.
        # If the player has hit all of the computer's ships, a winning message is displayed, and the game ends.
        if player_turn(computer_board):
            if check_win(computer_board, selected_ships):
                print("Congratulations! You have defeated the computer!")
                break
        
        # Checks if the computer's turn results in a hit on the player's board.
        # If the computer has hit all of the player's ships, a losing message is displayed, and the game ends.
        if computer_turn(player_board):
            if check_win(player_board, selected_ships):
                print("The computer won! Better luck next time!")
                break

# Checks if the script is being run directly and, if so, starts the main function.
if __name__ == "__main__":
    main()