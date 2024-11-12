# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#Possible ship types and their length
POSSIBLE_SHIPS = {
    5: {'S': 1, 'D': 2, 'C': 3}, # 5x5: 2-3 ships, längder 1-3
    8: {'S': 2, 'D': 3, 'C': 4}, # 8x8: 3-4 ships, längder 2-4
    10: {'S': 2, 'D': 3, 'C': 4, 'B': 5}, # 10x10: 4-5 ships, längder 2-5
    12: {'S': 2, 'D': 3, 'C': 4, 'B': 5} # 12x12: 5-7 ships, längder 2-5
}
# Player have to choose a gameboard size.
def get_board_size():
    while True:
        try:
            size = int(input("Välj spelplanens storlek (5, 8, 10, 12): "))
            if size in POSSIBLE_SHIPS:
                return size
            else:
                print("Ange ett giltigt val: 5, 8, 10 eller 12.")
        except ValueError:
            print("Ogiltig inmatning! Ange ett nummer mellan 5 och 12.")
# Player choose amont of ships to the boardsize player have chosen.
def choose_ships(size):
    max_ships = {5: (2, 3), 8: (3, 4), 10: (4, 5), 12:(5, 7)}
    min_ships, max_ships = max_ships[size]
    while True:
        try:
            num_ships = int(input(f"Välj antal skepp (mellan {min_ships} och {max_ships}): "))
            if min_ships <= num_ships <= max_ships:
                return dict(list(POSSIBLE_SHIPS[size].items())[:num_ships])
            else:
                print(f"Ange ett antal mellan {min_ships} och {max_ships}.")
        except ValueError:
            print("Ogiltig inmatning: Ange ett heltal.")
# The creation av the board
def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]
# The board will be printed to the screen
def print_board(board, reveal=False):
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            row_display.append(cell if reveal or cell in ['X', '0'] else '~')
        print(f"{i} " + " ".join(row_display))
# Code for placing ships: allows the player to select positions for their ships,
def place_ship_manually(board, ship_type, length):
    size = len(board)
    print(f"\nPlacera skeppet '{ship_type}' som är {length} rutor långt.")
    placed = False
    while not placed:
        try:
            row, col = map(int, input("Ange startposition för skeppet (rad kolumn): ").split())
            direction = input("Ange riktning  (h för horisontell, v för vertikal): ").lower()
            if direction == 'h' and col + length <= size:
                if all(board[row][col + i] == '~' for i in range(length)):
                    for i in range(length):
                        board[row][col + i] = ship_type
                    placed = True
                else:
                    print("Platsen är redan upptagen. Försök igen.")
            elif direction == 'v' and row + length <= size:
                if all(board[row + i][col] == '~' for i in range(length)):
                    for i in range(length):
                        board[row + i][col] = ship_type
                    placed = True
                else:
                    print("Platsen är redan upptagen. Försök igen.")
            else:
                print("Ogiltig position eller riktning. Försök igen.")
        except (ValueError, IndexError):
            print("Felaktig inmatning! Försök igen.")
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
            if all(board[row][col + 1] == '~' for i in range(length)):
                for i in range(length):
                    board[row][col + i] = 'S'
                placed = True
        else:
            row, col = random.randint(0, size - length), random.randint(0, size - 1)
            if all(board[row + i][col] == '~' for i in range(length)):
                for i in range(length):
                    board[row + i][col] = 'S'
                placed = True
# and the program will place the computers ships.
def place_all_ships_computer(board, ships):
    for ship, length in ships.items():
        place_ship_computer(board, length)
# Code that handles the player's turn to choose a target
def player_turn(board):
    print("\nDin tur! Använd formatet rad kolumn (t.ex. 2 3)")
    try:
        row, col = map(int, input("Ange rad och kolumn: ").split())
        if board[row][col] in POSSIBLE_SHIPS[5].keys():
            board[row][col] = 'X'
            print("Träff!")
            return True
        elif board[row][col] == '~':
            board[row][col] = '0'
            print("Miss!")
            return False
        else:
            print("Redan använt! Försök igen.")
            return player_turn(board)
    except (ValueError, IndexError):
        print("Felaktig inmatning! Försök igen.")
        return player_turn(board)
# Code that handles the computer's turn to choose a target.
def computer_turn(board):
    size = len(board)
    row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    while board[row][col] in ['X', 'O']:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
    if board[row][col] in POSSIBLE_SHIPS[5].keys():
        board[row][col] = 'X'
        print(f"Datorn träffade på {row} {col}!")
        return True
    else:
        board[row][col] = 'O'
        print(f"Datorn missade på {row} {col}.")
        return False

def check_win(board, ship):
    return all(cell not in ships.keys() for row in board for cell in row)

def main():
    print("Välkommen till Battleship!")
    board_size = get_board_size()
    player_board = create_board(board_size)
    computer_board = create_board(board_size)

    # Välj skepp baserat på brädstorleken
    selected_ships = choose_ships(board_size)

    # PLacera spelarnas skepp
    place_all_ships_manually(player_board, selected_ships)
    place_all_ships_computer(computer_board, selected_ships)

    while True:
        print("\nDitt bräde:")
        print_board(player_board, reveal=True)
        print("\Datorns bräde:")
        print_board(computer_board)

        if player_turn(computer_board):
            if check_win(computer_board, selected_ships):
                print("Grattis! Du har besegrat datorn!")
                break
        
        if computer_turn(player_board):
            if check_win(player_board, selected_ships):
                print("Datorn vann! Bättre lycka nästa gång!")
                break

if __name__ == "__main__":
    main()