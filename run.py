import random
import time

scores = {"computer": 0, "player": 0}
guessed_shot_player_0 = set() # set that contains the guesses made by the player
guessed_shot_computer = set() # set that contains the guesses made by the computer
player_initial_selection = set() # set that contains the ships coordinates for the player
computer_initial_selection = set() # set that contains the ships coordinates for the computer

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
            self.num_ships = num_ships
            self.player_name = player_name
            self.type = type
            self.board = [] # the board is an empty list
            self.delim_display = ""

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
            computer_initial_selection = set(initial_placement_computer) # It adds the coordinates randomly selected of the ships into the set.
            self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  self.board[initial_placement_computer[tple][0]][initial_placement_computer[tple][1]] = "X"  # it places the ships on the board
            
            self.display_board_info("Computer") #to be removed for test purpose                      
            self.format_display_board() #to be removed for test purpose 
                                    
            return self.board
         
      def initial_display_board_plr(self):
            """
            The method will place the random generated ships placement
            on the board for the player.
            """
            global player_initial_selection
            
            initial_placement_player = self.initial_placement_ships() # It creates a list of tuple composed of rows(R) and columns(C) for the player
            player_initial_selection = set(initial_placement_player) # It adds the coordinates randomly selected of the ships into the set.
            self.board = [["." for x in range(self.board_size)] for y in range(self.board_size)] # empty board without the ships

            for tple in range(self.num_ships):
                  self.board[initial_placement_player[tple][0]][initial_placement_player[tple][1]] = "X"  # it places the ships on the board
            
            self.display_board_info("Player")      
            self.format_display_board() # This line will display the board       
                        
            return self.board

      def display_board_info(self, player_type):
            """
            The method creates a header for the computer board and
            the player board.
            """
            self.player_type = player_type
            if self.board_size == 5:
                  self.delim_display = ('=' * 17)
            elif self.board_size == 6:
                  self.delim_display = ('=' * 21)  
            else:
                  self.delim_display = ('=' * 25)
            
            print(self.delim_display)
            if self.player_type == "Computer":
                  print("Computer Board")           
            else:
                  print("Player Board")
            print(self.delim_display)                                    

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
        if int(value) not in range(1, board_size+1):
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
          print(f"You have already used these numbers Row: {selection[0] + 1} and Column: {selection[1] + 1}. ")
          return False  
    
    return True

def call_shot_player(board_size):
    """
    The function allows the player to make guess by
    selecting a row and a column.
    """
    global guessed_shot_player_0
    
    while True:
          while True:
                print(f"Select a Row Number between 1 and {board_size} included")
                row_num_plr = input()
                if validate_integer_grid(row_num_plr, board_size): # Check if the row is an integer.
                      break
          
          while True:
                print(f"Select a Column Number between 1 and {board_size} included")
                column_num_plr = input()
                if validate_integer_grid(column_num_plr, board_size): # Check if the column is an integer.
                      break
          
          selection_0 = int(row_num_plr) - 1, int(column_num_plr) - 1 # It gives a tuple composed of a row and a column based on 0-indexing.
          selection_1 = int(row_num_plr), int(column_num_plr) # It gives a tuple composed of a row and a column based on 0-indexing.
          if validate_guess_already_used(selection_0, guessed_shot_player_0): # Check if the selection has been already used.
                break
                       
    return selection_0, selection_1
    
def call_shot_computer(board_size):
    """
    The function allows a random selection of a row
    and a column for the computer.
    """
    global guessed_shot_computer
    
    while True:
          row_num_cpt = random_integer(board_size)
          column_num_cpt = random_integer(board_size)
          selection = row_num_cpt, column_num_cpt
          
          if selection not in guessed_shot_computer: # Check if the selection has been already used.
                break

    return row_num_cpt, column_num_cpt

def right_guess_or_not_plr(value):
    """
    The function checks the guesses made by the player,
    against the computer board.
    """
    global computer_initial_selection, scores
        
    if value in computer_initial_selection:
        scores["player"] = +1
        value = (value[0] + 1, value[1] + 1) # The value is based on the 0-indexation and changed to 1-indexation for visual representation
        return print(f"You sank an enemy ship at {value}.")
    else:
        return print("You missed, better luck next time")

def right_guess_or_not_cpt(value): 
    """
    The function checks the guesses made by the computer,
    against the player board.
    """
    global player_initial_selection, scores
    
    if value in player_initial_selection:
        scores["computer"] = +1
        value = (value[0] + 1, value[1] + 1) # The value is based on the 0-indexation and changed to 1-indexation for visual representation. Second change.
        return print(f"Your ship at {value} has been sunk")
    else:
        return print("The computer failed to sink any of your ships")
        
def display_score(player_name):
      """
      The function displays score at each iteration i.e after each
      computer and player guesses.
      """
      global computer_initial_selection, scores
      
      print("Score")
      print('=' * 35)
      print(f"Computer: {scores['computer']} | {player_name}: {scores['player']}")
      print('=' * 35)
    
def game_exit(num_ships):
      """
      The function manages the scenarios when the game ends.
      """
      global guessed_shot_player_0, guessed_shot_computer, player_initial_selection, computer_initial_selection, scores
            
      if len(guessed_shot_player_0|player_initial_selection) == (num_ships ** 2) or len(guessed_shot_computer|computer_initial_selection) == (num_ships ** 2):
            # The condition to end game is to cover the all grid 36 selections for a 6-size board and 49 for for a 7-size
            print(f"The game has ended. You covered the all grid. The final score is {scores}.")
            return True
      elif len((guessed_shot_player_0&player_initial_selection)) == num_ships:         
            # The condition to end game is that the player makes the right guesses
            print(f"The game has ended. You sank all the computer's battleships. The final score is {scores}.")
            return True
      elif len((guessed_shot_computer&computer_initial_selection)) == num_ships:       
            # The condition to end game is that the computer makes the right guesses
            print(f"The game has ended. The computer sank all your battleships. The final score is {scores}.")
            return True

      print("condition 1 player:", guessed_shot_player_0|player_initial_selection) # to be removed - for testing purpose only.
      print(len(guessed_shot_player_0|player_initial_selection)) # to be removed - for testing purpose only.
      print("condition 1 computer:", guessed_shot_computer|computer_initial_selection) # to be removed - for testing purpose only.
      print(len(guessed_shot_computer|computer_initial_selection)) # to be removed - for testing purpose only.
      print("condition 2:", guessed_shot_player_0&player_initial_selection) # to be removed - for testing purpose only.
      print("condition 3:", guessed_shot_computer&computer_initial_selection) # to be removed - for testing purpose only. 
          
      return False


def new_game():
    """
    The function starts a new game. It gives an introductory text.
    It also runs all function of the program.
    """
    global scores, guessed_shot_player_0, guessed_shot_computer, player_initial_selection, computer_initial_selection
    
    print(
        """
        +======================================+
        | Welcome to ULTIMATE BATTLESHIPS!!    |
        | Top left corner is row: 1, col: 1    |
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
    board.initial_display_board_plr()
    board.initial_display_board_cpt()
    print()
    guessed_shot_player_1 = []
    while True:
          print()
          player_guess_0, player_guess_1 = call_shot_player(board_size)
          computer_guess = call_shot_computer(board_size)
          guessed_shot_player_0.add(player_guess_0)
          guessed_shot_computer.add(computer_guess)         
          print(guessed_shot_player_0) # to be removed - for testing purpose only.
          print(guessed_shot_computer) # to be removed - for testing purpose only.
          print()          
          print("Outcome:")
          print('=' * 35)
          right_guess_or_not_plr(player_guess_0) # Check if the guess made by the player is correct
          right_guess_or_not_cpt(computer_guess) # Check if the guess made by the computer is correct
          print('=' * 35)
          print()
          display_score(player_name)
          guessed_shot_player_1.append(player_guess_1) # Selection made the player added to a list based on 1-indexing
          print("You selected Rows and Columns (R,C):\n", guessed_shot_player_1)
          print('=' * 35)
          print()
          
          if game_exit(num_ships):
                break
    
new_game()