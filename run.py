import random
import time

scores = {"computer": 0, "player": 0}
guessed_shot = set()
player_initial_selection = set()
computer_initial_selection = set()

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
            self.board = [] # the board is an empty list
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
            global computer_initial_selection
            initial_placement_computer = self.initial_placement_ships() # It creates a list of tuple composed of rows(R) and columns(C) for the computer
            computer_initial_selection = set(initial_placement_computer) # It adds the coordinates randomly selected on the shsips into the set.
            self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  self.board[initial_placement_computer[tple][1]][initial_placement_computer[tple][0]] = "X"  # it places the ships on the board
            
            self.display_board_info("Computer")                       
            self.format_display_board()
                                    
            return self.board
         
      def initial_display_board_plr(self):
            """
            The method will place the random generated ships placement
            on the board for the player.
            """
            global player_initial_selection
            
            initial_placement_player = self.initial_placement_ships() # It creates a list of tuple composed of rows(R) and columns(C) for the player
            player_initial_selection = set(initial_placement_player) # It adds the coordinates randomly selected on the shsips into the set.
            self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  self.board[initial_placement_player[tple][1]][initial_placement_player[tple][0]] = "X"  # it places the ships on the board
            
            self.display_board_info("Player")      
            self.format_display_board()        
                        
            return self.board

      def display_board_info(self, player_type):
            """
            The method creates a header for the computer board and
            the player board.
            """
            self.player_type = player_type
            if self.board_size == 5:
                  delim_display = ('=' * 17)
            elif self.board_size == 6:
                  delim_display = ('=' * 21)  
            else:
                  delim_display = ('=' * 25)
            
            print(delim_display)
            if self.player_type == "Computer":
                  print("Computer Board")           
            else:
                  print("Player Board")
            print(delim_display)            
                          

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
              if int(value) not in [6,7]:
                    raise ValueError
        except ValueError:
              print(f"Error: the board size is 6 or 7, you provided {value}, please try again.\n")
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
           board_size = input("Select a board size: 6 or 7\n")
           if validate_input_board(board_size):
                 break    

     while True:
           num_ships = input("Select a number of ships: 4,5 or 6\n")
           if validate_input_ships(num_ships):
                 break
           
     return player_name , int(board_size), int(num_ships)

def validate_integer_grid(value, board_size):
    """
    The function raises a ValueError if the number is not an
    integer or outside of the grid.
    """
    try:
        int(value)
        if int(value) not in range(1, board_size):
            raise ValueError
      
    except ValueError:
          print(f"The number is not an integer or within the range of 1 to {board_size} ")
          return False
    
    return True

def validate_guess_already_used(selection, guessed_shot):
    """
    The function raises a ValueError if the selection has already
    been used.
    """
    try:
          if selection in guessed_shot:
                raise ValueError

    except ValueError:
          print(f"You have already used these numbers Row: {selection[0]} and Column: {selection[1]}. ")
          return False  
    
    return True

def call_shot_player(board_size):
    """
    The function allows the player to make guess by
    selecting a row and a column.
    """
    global guessed_shot
    
    while True:
          while True:
                print(f"Select a Row Number between 1 and {board_size} included")
                row_num_plr = int(input()) - 1
                if validate_integer_grid(row_num_plr, board_size):
                      break
          
          while True:
                print(f"Select a Column Number between 1 and {board_size} included")
                column_num_plr = int(input()) - 1
                if validate_integer_grid(column_num_plr, board_size):
                      break
          
          selection = row_num_plr, column_num_plr
          if validate_guess_already_used(selection, guessed_shot):
                break
                       
    return row_num_plr, column_num_plr
    
def call_shot_computer(board_size):
    """
    The function allows a random selection of a row
    and a column for the computer.
    """    
    print("Row Selction from computer ")
    row_num_cpt = random_integer(board_size)
    print("Column Selction from computer")
    column_num_cpt = random_integer(board_size)

    return row_num_cpt, column_num_cpt

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
        |     -the board Size: 6 or 7          |
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
    print()
    player_selection = call_shot_player(board_size)
    computer_selection = call_shot_computer(board_size)
    
    print(guessed_shot)  # To be removed, it tests the code   
    guessed_shot.add(player_selection) # To be removed, it tests the code
    
    print(player_selection) # To be removed, it tests the code
    print(computer_selection) # To be removed, it tests the code
    print(guessed_shot) # To be removed, it tests the code
    print("player_initial_selection:", player_initial_selection) # To be removed, it tests the code
    print("computer_initial_selection:", computer_initial_selection) # To be removed, it tests the code
    
new_game()