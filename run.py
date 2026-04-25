from random import randint
import time

scores = {"computer": 0, "player": 0}

class Board:
      """
      Description of the class
      """
      
      def __init__(self, board_size, num_ships, player_name, type):
          self.board_size = board_size
          self.board =  [["." for x in range(board_size)] for y in range(board_size)]
          self.board_size = board_size
          self.num_ships = num_ships
          self.player_name = player_name
          self.type = type

      def display_board(self):
          return [print("   ".join(row)) for row in self.board]
              

def validate_input_player(value):
        """
        The function raises a ValueError if the player name is an empty string,
        but allow special character except space.
        """
        try:
              if value == '' or value.isspace():
                    raise ValueError(
                          f"The name should contain at least a charcater"
                    )
        except ValueError as e:
              print(f"Invalid data: {e}, please try again.\n")
              return False
        
        return True


def validate_input_board(value):
        """
        The function raises a ValueError if board Size is not 5,6 or7.
        """
        try:
              int(value)
              if int(value) not in [5,6,7]:
                    raise ValueError
        except ValueError:
              print(f"Error: the board size is 5,6 or 7, you provided {value}, please try again.\n")
              return False  
    
        return True


def validate_input_ships(value):
        """
        The function raises a ValueError if A number of Ships is not 4,5 or 6.
        """
        try:
              int(value)
              if int(value) not in [4,5,6]:
                    raise ValueError
        except ValueError:
              print(f"Error: the number of ships is 4,5 or 6, you provided {value}, please try again.\n")
              return False  
    
        return True


def input_player():
     """
    The function allowes the input of:
    the player's name, size of the board and number of ships. 
    """
     while True:
           player_name = input("Please enter your name:\n").capitalize()
           if validate_input_player(player_name):
                 break

     while True:
           board_size = input("Select a board size: 5,6 or 7\n")
           if validate_input_board(board_size):
                 break    

     while True:
           num_ships = input("Select a number of ships: 4,5 or 6\n")
           if validate_input_ships(num_ships):
                 break
           
     return player_name , int(board_size), int(num_ships)


def random_integer(board_size):
    """
    The function will provide a random integer for the computer turn
    """
    return randint(0, board_size - 1)


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
    board = Board(board_size, num_ships, player_name, "X")
    print()
    print('=' * 35)
    print(f"WELCOME TO THE GAME {player_name}")
    print(f"You selected a board size of {board_size}")
    print(f"Each player will have {num_ships} battleships")
    print('=' * 35)
    print()
    board.display_board()
    print()
    print(random_integer(board_size))

new_game()