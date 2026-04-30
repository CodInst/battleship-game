import random
import time

scores = {"computer": 0, "player": 0}

def random_integer(value):
    """
    The function will provide a random integer for the computer turn
    """
    return random.randint(0, value - 1)

class Board:
      """
      Description of the class
      """
      def __init__(self, board_size, num_ships, player_name, type):
            self.board_size = board_size
            self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)]
            self.num_ships = num_ships
            self.player_name = player_name
            self.type = type

      def format_display_board(self):
          return [print("   ".join(row)) for row in self.board]
      
      def initial_placement_ships(self):
            """
            The method will create a initial random placement of ships on
            the board for the player and the computer.
            """
            initial_board_row = random.sample(range(0, self.board_size), self.num_ships)  # Generate unique random numbers for the rows in a list
            initial_board_column = random.sample(range(0, self.board_size), self.num_ships)  # Generate unique random numbers for the columns in a list
            initial_board = list(zip(initial_board_row, initial_board_column))

            return  initial_board # It creates a list of tuple composed of rows(R) and columns(C). [(R1,C1), (R2,C2), (R3,C3),...]
              
      def initial_display_board_cpt(self):
            """
            The method will place the random generated ships placement
            on the board for the computer.
            """
            initial_placement_computer = self.initial_placement_ships() # It creates a list of tuple composed of rows(R) and columns(C) for the computer
            computer_board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  computer_board[initial_placement_computer[tple][1]][initial_placement_computer[tple][0]] = "X"  # it places the ships on the board

            self.display_board_info("Computer")                       
            self.board = computer_board
            computer_board = self.format_display_board()
                                    
            return computer_board
         
      def initial_display_board_plr(self):
            """
            The method will place the random generated ships placement
            on the board for the player.
            """
            initial_placement_player = self.initial_placement_ships() # It creates a list of tuple composed of rows(R) and columns(C) for the player
            player_board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  player_board[initial_placement_player[tple][1]][initial_placement_player[tple][0]] = "X"  # it places the ships on the board
            
            self.display_board_info("Player")      
            self.board = player_board
            player_board = self.format_display_board()        
                        
            return player_board

      def display_board_info(self, player_type):
            """
            The method creates a header for the computer board and
            the player board.
            """ 
            print('=' * 17)            
            if player_type == "Computer":
                  print("Computer Board")               
            else:
                  print("Player Board")
            print('=' * 17)
                              
            

def initial_validate_input_player_name(value):
        """
        The function raises a ValueError if the player name is an
        empty string but allow special character except space.
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


def initial_input_player():
     """
    The function allowes the input of:
    the player's name, size of the board and number of ships. 
    """
     while True:
           player_name = input("Please enter your name:\n").capitalize()
           if initial_validate_input_player_name(player_name):
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
    player_name, board_size, num_ships = initial_input_player()
    board = Board(board_size, num_ships, player_name, "X")
    print()
    print('=' * 35)
    print(f"WELCOME TO THE GAME, {player_name}")
    print(f"You selected a board size of {board_size}")
    print(f"Each player will have {num_ships} battleships")
    print('=' * 35)
    print()
    board.initial_display_board_cpt() # To be removed, it tests the code
    print()
    board.initial_display_board_plr()

new_game()