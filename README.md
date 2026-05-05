# Ultimate BattleShips
## Table of Contents

1. <a>[About](#about)</a>
2. <a>[Termminology](#terminology)</a>
3. <a>[Live Project](#live-project)</a>
4. <a>[Deployment Github](#deployment-github)</a>
5. <a>[Design Overview](#design-overview)</a>
6. <a>[Design Breakdown](#design-breakdown)</a>
7. <a>[Code Structure](#code-structure)</a>
      - <a>[Main Approach](#main-approach)</a>
      - <a>[Global Variables](#global-variables)</a>
      - <a>[Data Structures](#data-structures)</a>
      - <a>[Comments and Descriptions](#comments-and-descriptions)</a>
      - <a>[Libraries](#libraries)</a>
      - <a>[Functions and Instance Methods](#functions-and-instance-methods)</a>
      - <a>[Input Validation](#input-validation)</a>
7. <a>[Deployment Heroku](#deployment-heroku)</a>
      - <a>[Preparation](#preparation)</a>
      - <a>[Add Buildpacks](#add-buildpacks)</a>
      - <a>[Connect GitHub](#connect-gitHub)</a>
      - <a>[Automatic Deployment](#automatic-deployment)</a>
      - <a>[Deploy Main Branch](#deploy-main-branch)</a>
      - <a>[Open App](#open-app)</a>
8. <a>[Testing](#testing)</a>
9. <a>[Addtional Features](#addtional-features)</a>
10. <a>[Credits](#credits)</a>

# About

The ultimate battleship is a remake of the battleship game using a board displayed on a console.
Each player, a human versus a computer, takes turns to guess the warship’s location of the opposite side, concealed from one another. The objective is to destroy the opposing player’s battleships.

In this version of the game, the human player put in his name, can select two sizes of boards and the number of warships. The warships on the player’s board are marked with an ‘X’, while the computer’s board is concealed. The board is indexed on 1 unlike the python’s data structure such list.

The game will request you to enter a row number and column number. After the input, the computer will generate its own random row and column. The game will provide an outcome i.e. if the guess for each player was successfully or not. Finaly, a score is display at each iteration and the past guesses made by the player.

<a align="right">[Return Top](#table-of-contents)</a>

# Terminology

I use rows (R) and columns (C) for the coordinates instead of <strong>x</strong> and <strong>y</strong> regarding the location of the warships.<br>
I use a board input and board output based on <strong>1-indexing</strong>. The visual representation is also <strong>1-indexing</strong>.<br>
The processing, within the code, is <strong>0-indexing</strong>.

<a align="right">[Return Top](#table-of-contents)</a>

# Live Project

<a href="https://ultimate-battleships-05080b199617.herokuapp.com/" target="_blank">Live Project</a>

<a align="right">[Return Top](#table-of-contents)</a>

# Deployment GitHub

Using Github and Microsoft Visual Code to deploy my project.

### **Project setup in GitHub**

1. To setup the repository, I used <a href="https://github.com/Code-Institute-Org/p3-template" target="_blank">the code institute template</a>
2. I created a new public local repository on my Github account. I copied the repository locally on my computer using Microsoft Visual Code.
3. I used the command <strong><em>git clone https://github.com/CodInst/battleship-game.git</em></strong> in Microsoft-Visual-Code terminal.
4. I created and activated the virtual environment:
<img width="472" height="751" alt="Image" src="https://github.com/user-attachments/assets/e436d720-a6ec-4354-b0b7-76f715bd63ac" />
<br>
5. To confirm, it is activated, you should see <strong><em>.venv</em></strong> at the bottom of Microsoft Visual Code.
<img width="838" height="112" alt="Image" src="https://github.com/user-attachments/assets/91e4a98d-2f28-41fe-a69a-edb60a01e7f2" />
<br>
6. In my local copy, I created the  file <strong><em>.gitignore</em></strong>. I added <strong><em>.venv</em></strong> within the file and save it.

### **Working with My Repository**

1. Regularly and repeatedly, I committed my changes to my local repository with commands below. Each commit has its custom message.
      - <strong>git add .</strong>
      - <strong>git commit -m "Custom message"</strong>
2. Finally pushing my commits to my remote repository by using the command below.
      - <strong>git push</strong>

<a align="right">[Return Top](#table-of-contents)</a>

# Design Overview

Based on the project-scope-3 video produced by Code Insitute, I designed in Miscrosoft Visio, a flow chart describing the steps:
<img width="601" height="847" alt="Image" src="https://github.com/user-attachments/assets/13e55f4e-abcb-4be9-b03d-f7ce8e5b9e10" />

<a align="right">[Return Top](#table-of-contents)</a>

# Design Breakdown

To tackle the project, I decided break down the project into smaller steps, as shown below:
<img width="593" height="851" alt="Image" src="https://github.com/user-attachments/assets/a876cc88-20e7-4810-bfb7-897703bfb0d0" />

<a align="right">[Return Top](#table-of-contents)</a>

# Code Structure

### Main Approach
I wanted to allow the input from player and the output displaying the outcomes to be based on <strong><em>1-indexing</em></strong> for user friendliness.<br>
The code, within, will be processed based on <strong><em>0-indexing</em></strong>.<br>
In the code below, for example:<br>
      -<strong><em>selection_0</em></strong> is <strong><em>0-indexing</em></strong>.<br>
      -<strong><em>selection_1</em></strong> is <strong><em>1-indexing</em></strong>.<br>

      def call_shot_player(board_size):
    """
    The function allows the player to make guess by
    putting-in a row and a column.
    """
    global guessed_shot_player_0
    
    while True:
          while True:
                print(f"Select a Row Number between 1 and {board_size} included")
                row_num_plr = input("\n")
                if validate_integer_grid(row_num_plr, board_size): # Check if the row is an integer.
                      break
          
          while True:
                print(f"Select a Column Number between 1 and {board_size} included")
                column_num_plr = input("\n")
                if validate_integer_grid(column_num_plr, board_size): # Check if the column is an integer.
                      break
          
          selection_0 = int(row_num_plr) - 1, int(column_num_plr) - 1 # It gives a tuple composed of a row and a column based on 0-indexing.
          selection_1 = int(row_num_plr), int(column_num_plr) # It gives a tuple composed of a row and a column based on 1-indexing.
          if validate_guess_already_used(selection_0, guessed_shot_player_0): # Check if the selection has been already used.
                break
                       
    return selection_0, selection_1

<a align="right">[Return Top](#table-of-contents)</a>

### Global Variables
I made use of five global variables.

      scores = {"computer": 0, "player": 0} # Dictionary to process the score
      guessed_shot_player_0 = set() # set that contains the guesses made by the player
      guessed_shot_computer = set() # set that contains the guesses made by the computer
      player_initial_selection = set() # set that contains the ships coordinates for the player
      computer_initial_selection = set() # set that contains the ships coordinates for the computer

<a align="right">[Return Top](#table-of-contents)</a>

### Data Structures
I used a multitude of data structures in order to explore their uses and implications in this project.

#### Class

      class Board:
      """
      The class Board takes in, the size of the board, the number
      of ships, the player's name. Methods to generate random,
      placements for the ships and place it in the board.
      """
      def __init__(self, board_size, num_ships, player_name):
            self.board_size = board_size
            self.num_ships = num_ships
            self.player_name = player_name
            self.board = [] # the board is an empty list
            self.delim_display = ""
      
#### Dictionary

      scores = {"computer": 0, "player": 0} # Dictionary to process the score
      
#### Set

      guessed_shot_player_0 = set() # set that contains the guesses made by the player
      guessed_shot_computer = set() # set that contains the guesses made by the computer
      player_initial_selection = set() # set that contains the ships coordinates for the player
      computer_initial_selection = set() # set that contains the ships coordinates for the computer
      
#### List

      guessed_shot_player_1 = [] # List of Guesses made by the player based on 1-indexing.
      
#### Tuple

      def initial_placement_ships(self):
            """
            The method creates a initial random placement of ships on
            the board for the player and the computer.
            """
            # Generate unique random numbers for the rows in a list
            # It creates a list of tuple composed of rows(R) and columns(C). [(R1,C1), (R2,C2), (R3,C3),...]
            return  list(zip(random.sample(range(0, self.board_size), self.num_ships), random.sample(range(0, self.board_size), self.num_ships)))

<a align="right">[Return Top](#table-of-contents)</a>

### Comments and Descriptions
I made an extensive use of comments across the code. I also include a description for each functions and methods

      def new_game():
    """
    The function starts a new game. It gives an introductory text.
    It also runs all function of the program.
    """
    global scores, guessed_shot_player_0, guessed_shot_computer, player_initial_selection, computer_initial_selection

<a align="right">[Return Top](#table-of-contents)</a>

### Libraries
I imported the library <strong>random</strong> and used two methods <strong><em>.randint()</em></strong> and <strong><em>.sample()</em></strong>.

      import random

<a align="right">[Return Top](#table-of-contents)</a>

### Functions and Instance Methods

#### The class Board includes five methods and one instance method.
<img width="536" height="333" alt="Image" src="https://github.com/user-attachments/assets/9cc83b29-1e07-4c39-811c-52151d4ac554" /><br>

#### The codes include a main function.
<img width="160" height="79" alt="Image" src="https://github.com/user-attachments/assets/32f85a42-e1c4-4835-8c3a-16f1194b5e40" /><br>

#### The codes include 13 functions.
<img width="484" height="459" alt="Image" src="https://github.com/user-attachments/assets/bed22bef-9fad-46bc-87a8-1940f5eda95f" /><br>
<img width="245" height="41" alt="Image" src="https://github.com/user-attachments/assets/42e1c8fe-8941-49c4-a47d-902d1615f2a0" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Input Validation
The code takes into account four types of input validations.

#### 1. Integer and Integer within the options offered - Board size / Number of Ships
The code will check if the input is an integer first and if the integer is within the options offered

<strong>Board szie</strong>
    
        def validate_input_board(value):
        """
        The function raises a ValueError if board Size is not an integer, the value 6 or value 7.
        """
        try:
              int(value)
              if int(value) not in [6,7]:
                    raise ValueError
        except ValueError:
              print(f"Error: the board size is 6 or 7, you provided {value}, please try again.\n")
              return False  
    
        return True

<strong>Number of Ships</strong>
    
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

#### 2. Selection of Rows and columns

      def call_shot_player(board_size):
    """
    The function allows the player to make guess by
    putting-in a row and a column.
    """
    global guessed_shot_player_0
    
    while True:
          while True:
                print(f"Select a Row Number between 1 and {board_size} included")
                row_num_plr = input("\n")
                if validate_integer_grid(row_num_plr, board_size): # Check if the row is an integer.
                      break
          
          while True:
                print(f"Select a Column Number between 1 and {board_size} included")
                column_num_plr = input("\n")
                if validate_integer_grid(column_num_plr, board_size): # Check if the column is an integer.
                      break
          
          selection_0 = int(row_num_plr) - 1, int(column_num_plr) - 1 # It gives a tuple composed of a row and a column based on 0-indexing.
          selection_1 = int(row_num_plr), int(column_num_plr) # It gives a tuple composed of a row and a column based on 1-indexing.
          if validate_guess_already_used(selection_0, guessed_shot_player_0): # Check if the selection has been already used.
                break
                       
    return selection_0, selection_1

#### 3. player name within the acceptance criteria

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

#### 4. Row and column already selected

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

<a align="right">[Return Top](#table-of-contents)</a>

# Deployment Heroku

### Preparation
1. The unused libraries were already removed. I am using only one library: random.<br>
2. I did not use any libraries such <strong><em>pprint</em></strong> or other commands that will be not recognise by <strong>Heroku</strong>.<br>
3. I added a character ‘\n’ line for each input to take into account the <strong>Heroku</strong> console.<br>
4. I created a requirement file with the command <strong><em>pip3 freeze > requirements.txt</em></strong><br>
5. I saved last modifications of the file to GitHub with a last <strong><em>git push</em></strong>.<br>

<a align="right">[Return Top](#table-of-contents)</a>

### Create an App

I logged in on Heroku and created an app via the main dashboard.<br>
<img width="1055" height="157" alt="Image" src="https://github.com/user-attachments/assets/2f8cfd42-2f5f-4453-b481-065ad1b6fdad" /><br>
<img width="641" height="525" alt="Image" src="https://github.com/user-attachments/assets/bda83ad2-0590-4cdb-a344-ed922a17f4f6" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Add Buildpacks

I navigated to <strong>settings</strong> and added the following buildpacks: <strong><em>Python</em></strong> and <strong><em>NodeJS</em></strong>.<br>
<img width="973" height="261" alt="Image" src="https://github.com/user-attachments/assets/e8daf5f5-f887-494e-ab45-3bc42139bab6"/><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Connect GitHub

I navigated to <strong>deploy</strong> and performed the following actions.<br>
I connected it to my GitHub and select my repository.<br>
<img width="709" height="330" alt="Image" src="https://github.com/user-attachments/assets/75f0d10b-fde3-407e-b051-7e39ecdc8f37" /><br>
<img width="716" height="131" alt="Image" src="https://github.com/user-attachments/assets/19441c5b-2aa3-4fa9-beeb-0ce89c133730" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Automatic Deployment

I allowed <strong>automatic deployment</strong> as the project has been thoroughly tested.<br>
<img width="622" height="251" alt="Image" src="https://github.com/user-attachments/assets/4643c5df-fb41-48db-a2db-1e074adaa9b3" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Deploy Main Branch

I deployed <strong>the main branch</strong>.<br>
<img width="717" height="338" alt="Image" src="https://github.com/user-attachments/assets/48b5ff1f-21d5-4a27-988a-5dcc283680e0" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

### Open App

I opened the app and test it out.
<img width="669" height="445" alt="Image" src="https://github.com/user-attachments/assets/bfd21093-6315-4341-9414-77fd13e4ba91" /><br>

<a align="right">[Return Top](#table-of-contents)</a>

# Testing

### Manual Testing
I performed a manual testing along the coding process with most of time with print message.<br>
I put in place the final loop within new_game() only at the end to allow an easy troubleshooting.<br>

<a align="right">[Return Top](#table-of-contents)</a>

# Addtional Features

### Timer
I was hoping to have time to include a 15-minutes timer to end the game but ran out of time.<br>
Please find below a glimpse of the potential code to implement.<br>

      import time


    time_starting = time.time_ns()
    hour_starting = time.localtime()[3]
    minutes_starting = time.localtime()[4]
    game_time = 900
    game_end = False
    # Start game
    print(f"Your game started at {hour_starting}.{minutes_starting}, It will end in 15 minutes.")

    # at each iteration
    time_elapsed = time.time_ns() - time_starting

    # loop checker
    While game_end == False:
        # game
        time_elapsed = time.time_ns() - time_starting
        if time_elapsed >= game_time:
            game_end = True

    
### Display the board
Displaying the player's board at each iteration could have added a value to the user-experience.
    
<a align="right">[Return Top](#table-of-contents)</a>

# Credits

The design of the project was drafted based on the guidelines provided in the code-institute project scope. Particularly the video.

<a align="right">[Return Top](#table-of-contents)</a>
