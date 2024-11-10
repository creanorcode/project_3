# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#Possible ship types and their length
POSSIBLE_SHIPS = {
    5: {'S': 1, 'D': 2, 'C': 3}, # 5x5: 2-3 ships, längder 1-3
    8: {'S': 2, 'D': 3, 'C': 4}, # 8x8: 3-4 ships, längder 2-4
    10: {'S': 2, 'D': 3, 'C': 4, 'B': 5}, # 10x10: 4-5 ships, längder 2-5
    12: {'S': 2, 'D': 3, 'C': 4, 'B': 5} # 12x12: 5-7 ships, längder 2-5
}

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

def create_board(size):
    return [['~' for _ in range(size)] for _ in range(size)]

def print_board(board, reveal=False):
    size = len(board)
    print("  " + " ".join(str(i) for i in range(size)))
    for i, row in enumerate(board):
        row_display = []
        for cell in row:
            row_display.append(cell if reveal or cell in ['X', '0'] else '~')
        print(f"{i} " + " ".join(row_display))
        