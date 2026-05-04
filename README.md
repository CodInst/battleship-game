# Ultimate BattleShips - Table of Contents

1. <a>[About](#about)</a>
1. <a>[Termminology](#terminology)</a>
2. <a>[Live Project](#live-project)</a>
3. <a>[Deployment](#deployment)</a>
4. <a>[Design Draft](#design-draft)</a>
5. <a>[Design Final](#design-final)</a>
6. <a>[Colours](#colours)</a>
8. <a>[Fonts](#fonts)</a>
7. <a>[Features](#features)</a>
8. <a>[Codes](#codes)</a>
9. <a>[Testing](#testing)</a>
      - <a>[Testing with W3C CSS](#testing-with-w3c-css)</a>
      - <a>[Testing with W3C HTML](#testing-with-w3c-html)</a>
      - <a>[Testing with Chrome Lighthouse](#testing-with-chrome-lighthouse)</a>
10. <a>[Project Revision and Manual Testing](#project-revision-and-manual-testing)</a>
11. <a>[Credits](#credits)</a>

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

[Link](https://ultimate-battleships-05080b199617.herokuapp.com/)
<a https://ultimate-battleships-05080b199617.herokuapp.com/">Live Project</a>

<a align="right">[Return Top](#table-of-contents)</a>

# Deployment
