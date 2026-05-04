# Ultimate BattleShips - Table of Contents

1. <a>[About](#about)</a>
2. <a>[Termminology](#terminology)</a>
3. <a>[Live Project](#live-project)</a>
4. <a>[Deployment Github](#deployment-github)</a>

X. <a>[Design Draft](#design-draft)</a>
X. <a>[Design Final](#design-final)</a>
X. <a>[Colours](#colours)</a>
X. <a>[Fonts](#fonts)</a>
X. <a>[Features](#features)</a>
X. <a>[Codes](#codes)</a>
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

I use rows (R) and columns (C) for the coordinates x and y regarding the location of the warships.<br>
I use a board input and board output based on 1-indexing. The visual representation is also 1-indexing.<br>
The processing, within the code, is 0-indexing.

<a align="right">[Return Top](#table-of-contents)</a>

# Live Project

<a href="https://ultimate-battleships-05080b199617.herokuapp.com/" target="_blank">Live Project</a>

<a align="right">[Return Top](#table-of-contents)</a>

# Deployment GitHub

Using Github and Microsoft Visual Code to deploy my project

### **My Repository**

1. Created a new public local repository on my Github account, and copied the repository locally on my computer using Microsoft Visual Code to start building the website.
2. Regularly and repeatedly, I committed my changes to my local repository with commands below. Each commit has its custom message.
      - <strong>git add .</strong>
      - <strong>git commit -m "Custom message"</strong>
3. Finally pushing my commits to my remote repository by using the command below.
      - <strong>git push</strong>

### **Hosting**

1. To start working on my website, I went onto Github and selected my repository named <strong>battleship-game</strong>.
2. I went to Settings > Pages
3. I made sure the following settings were applied:
      - Source: 'Deploy from a branch' on the dropdown menu
      - Branch: 'Main' and 'root' from the dropdown menus
      - Entered save

### **Deployment on Github**

<a align="right">[Return Top](#table-of-contents)</a>

