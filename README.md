# Rock Paper Scissors

A simple command-line implementation of the classic rock paper scissors game in Python.

## How to Play

When you run the program, you will be prompted to enter either "rock", "paper", or "scissors". The computer will then randomly choose between those three options. 

The winner is determined by the classic rules:

- Rock smashes scissors
- Scissors cut paper  
- Paper covers rock

If both players choose the same option, it results in a tie.

The program will keep track of wins, losses and ties. It will ask if you want to play again after each round.

## Code Overview

The code consists of the following key functions:

- `get_user_choice()` - Gets the user's choice and validates input
- `get_computer_choice()` - Randomly chooses between rock, paper or scissors
- `determine_winner()` - Compares the user and computer choices and determines the winner
- `play_game()` - The main game loop that runs each round

The game also utilizes ANSI escape codes to print colored text to the terminal for a better user experience.

## To Run

Simply run the Python file:

```
python rock_paper_scissors.py
```
