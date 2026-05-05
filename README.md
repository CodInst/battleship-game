# Ultimate BattleShips - Table of Contents

1. <a>[About](#about)</a>
2. <a>[Termminology](#terminology)</a>
3. <a>[Live Project](#live-project)</a>
4. <a>[Deployment Github](#deployment-github)</a>
5. <a>[Design Overview](#design-overview)</a>
6. <a>[Design Breakdown](#design-breakdown)</a>
7. <a>[Deployment Heroku](#deployment-heroku)</a>
      - <a>[Testing with W3C CSS](#testing-with-w3c-css)</a>
      - <a>[Testing with W3C HTML](#testing-with-w3c-html)</a>
      - <a>[Testing with Chrome Lighthouse](#testing-with-chrome-lighthouse)</a>
8. <a>[Project Revision and Manual Testing](#project-revision-and-manual-testing)</a>
9. <a>[Credits](#credits)</a>

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

# Deployment Heroku

<img width="1055" height="157" alt="Image" src="https://github.com/user-attachments/assets/2f8cfd42-2f5f-4453-b481-065ad1b6fdad" />

<img width="641" height="525" alt="Image" src="https://github.com/user-attachments/assets/bda83ad2-0590-4cdb-a344-ed922a17f4f6" />

<img width="973" height="261" alt="Image" src="https://github.com/user-attachments/assets/e8daf5f5-f887-494e-ab45-3bc42139bab6" />

<img width="709" height="330" alt="Image" src="https://github.com/user-attachments/assets/75f0d10b-fde3-407e-b051-7e39ecdc8f37" />

<img width="716" height="131" alt="Image" src="https://github.com/user-attachments/assets/19441c5b-2aa3-4fa9-beeb-0ce89c133730" />

<img width="622" height="251" alt="Image" src="https://github.com/user-attachments/assets/4643c5df-fb41-48db-a2db-1e074adaa9b3" />

<img width="717" height="338" alt="Image" src="https://github.com/user-attachments/assets/48b5ff1f-21d5-4a27-988a-5dcc283680e0" />

<img width="669" height="445" alt="Image" src="https://github.com/user-attachments/assets/bfd21093-6315-4341-9414-77fd13e4ba91" />
