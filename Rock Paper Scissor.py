#########################################################################

# Importing a random library
import random


# getting the player Input
def player_choose():
    char_list = ['Stone', 'Paper', 'Scissor']
    player_choice = ''

    while player_choice.capitalize() not in char_list:
        player_choice = input("Enter your character (Stone, Paper, Scissor):- ")

    return player_choice.capitalize()


# Getting a computer Input with random Lib
def computer_choose():
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        return "Stone"

    elif comp_choice == 2:
        return 'Paper'

    elif comp_choice == 3:
        return "Scissor"


# Checking for win!
def check_win(player, computer):
    if (player == 'Stone') and (computer == 'Stone'):
        return '!! Tie !!'

    elif (player == 'Stone') and (computer == 'Paper'):
        return 'You Loose :('

    elif (player == 'Stone') and (computer == 'Scissor'):
        return '!! You Won !!'

    elif (player == 'Paper') and (computer == 'Paper'):
        return '!! Tie !!'

    elif (player == 'Paper') and (computer == 'Stone'):
        return '!! You Won !!'

    elif (player == 'Paper') and (computer == 'Scissor'):
        return 'You Loose :('

    elif (player == 'Scissor') and (computer == 'Scissor'):
        return '!! Tie !!'

    elif (player == 'Scissor') and (computer == 'Stone'):
        return 'You Loose :('

    elif (player == 'Scissor') and (computer == 'Paper'):
        return '!! You Won !!'


# Asking for want to play more
def replay():
    inp = ''

    while inp.capitalize() not in ['Yes', 'No']:
        inp = input('Do you want to play (Yes, No):- ')

    return inp.capitalize() == 'Yes'


# Main Game Loop
game_on = True

while game_on:

    p_move = player_choose()
    c_move = computer_choose()
    win = check_win(p_move, c_move)

    print(f'Your Move:- {p_move}')
    print(f'Computer Move:- {c_move}')
    print(win)

    if not replay():
        break

#############################################################################
