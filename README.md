# Ultimate BattleShips - Table of Contents

1. <a>[About](#about)</a>
2. <a>[Termminology](#terminology)</a>
3. <a>[Live Project](#live-project)</a>
4. <a>[Deployment Github](#deployment-github)</a>
5. <a>[Design Draft](#design-draft)</a>
X. <a>[Design Final](#design-final)</a>
X. <a>[Colours](#colours)</a>
X. <a>[Fonts](#fonts)</a>
X. <a>[Features](#features)</a>
X. <a>[Testing](#testing)</a>
      - <a>[Testing with W3C CSS](#testing-with-w3c-css)</a>
      - <a>[Testing with W3C HTML](#testing-with-w3c-html)</a>
      - <a>[Testing with Chrome Lighthouse](#testing-with-chrome-lighthouse)</a>
X. <a>[Project Revision and Manual Testing](#project-revision-and-manual-testing)</a>
x. <a>[Credits](#credits)</a>

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

Using Github and Microsoft Visual Code to deploy my project

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

