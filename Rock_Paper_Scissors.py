
import random

def getFrom():
    user = input('Please enter rock, paper, or scissors: ').lower()
    while not (user == 'rock' or user == 'paper' or user == 'scissors'):
        print('Illegal input!')
        user = input('Enter rock, paper, or scissors: ').lower()
    return user

def createRandom():
    game_dict = {1: 'rock', 2: 'paper', 3: 'scissors'}
    return game_dict[random.randint(1, 3)]

def check(user_counter, computer_counter):
    user = getFrom()                # get the user's move.
    computer = createRandom()       # get the computer's move.
    print(f'The computer chose - \033[92m{computer}\033[0m')
    if user == 'rock' and computer == 'scissors':
        print('\033[92mYou won the game!\033[0m')
        user_counter.append(1)
    elif user == 'paper' and computer == 'rock':
        print('\033[92mYou won the game!\033[0m')
        user_counter.append(1)
    elif user == 'scissors' and computer == 'paper':
        print('\033[92mYou won the game!\033[0m')
        user_counter.append(1)
    elif user == computer:      # if it's a tie, print a message and not adding to the counter
        print('\033[94mYou tied! You can try again.\033[0m')
    else:                       # if the user loses, update the computer score
        print('\033[91mYou lost!\033[0m')
        computer_counter.append(1)
    continue_game(user_counter, computer_counter)

def continue_game(user_counter, computer_counter):
    decision = input('Do you want to continue? (Answer \033[92myes\033[0m to continu palying): ')
    if decision.lower() == 'yes':
        print('\033[93mGreat lets play again!\033[0m ')
        check(user_counter, computer_counter)       #wants to continu so call the fuction again
    else:
        print(f'you won \033[92m{len(user_counter)}\033[0m times!, and lost \033[91m{len(computer_counter)}\033[0m times.')
        print('\033[96m+++++++++ Good game! Hope to see you again! +++++++++\033[0m')

print('\033[96m+++++++ Hello and welcome to the game of rock, paper, and scissors! +++++++\033[0m')
# initialize counters to keep track of the user's wins and the computer's wins
user_counter = []
computer_counter = []
# starting the game
check(user_counter,computer_counter)


