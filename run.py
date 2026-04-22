def input_player():
     """
    The function allowes the input of:
    the player's name, size of the board and number of ships. 
    """
     player_name = input("Please enter your name:\n")
     board_size = int(input("Select a board size:5,6 or 7\n"))
     num_ships = int(input("Select a number of ships: 4,5 or 6\n"))

     return player_name, board_size, num_ships

def new_game():
    """
    The function starts a new game. It gives an introductory text.
    It runs all function of the program.
    """

    print(
        """
        +======================================+
        | Welcome to ULTIMATE BATTLESHIPS!!    |
        | Top left corner is row: 0, col:0     |
        | Select a number for:                 |
        |     -the board Size: 5,6 or 7        |
        |     -the number of Ships: 4,5 or 6   |
        +======================================+
        """)
    player_name, board_size, num_ships = input_player()

    return player_name, board_size, num_ships

print(new_game())