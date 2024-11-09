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
