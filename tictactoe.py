##### TIC TAC TOE: 
    ## 1) Create a Board of Blanks: 
    ## 2) Allow a User to select a Space that they want to play their letter in
    ## 3) Have the Computer Choose a Space Randomly
        ## Unless Specific Moves are Available
    ## 4) Determine a Winner
import random

game_board = {'7' : '_' , '8' : '_' , '9': '_' , 
              '4' : '_' , '5' : '_' , '6': '_' , 
              '1': '_' , '2' : '_' , '3': '_'}
first_play = None

def print_board(game_board): 
    print(game_board['7'] + '|' + game_board['8'] + '|' + game_board['9'])
    print('-+-+-')
    print(game_board['4'] + '|' + game_board['5'] + '|' + game_board['6'])
    print('-+-+-')
    print(game_board['1'] + '|' + game_board['2'] + '|' + game_board['3'])


def determine_first_turn():
    random_number = random.randint(0, 1)
    if random_number == 0:
        first_play = 'Player'
        print(first_play + " Goes First")
        return first_play
    else:
        first_play = 'Computer'
        print(first_play + " Goes First")
        return first_play

def computer_placement(game_board):
    print_board(game_board)
    
    random_number = random.randint(0, 3) 
    ## Goes After Winning Move First

    ## Blocks Winning Move Second

    ### Goes After Corner Slots if Open and No winning / Stop From Winning turns are available
    if random_number == 0 and game_board['7'] == '_':
        game_board['7'] = 'O'
        return game_board
    if random_number == 1 and game_board['9'] == '_':
        game_board['9'] = 'O'
        return game_board
    if random_number == 2 and game_board['1'] == '_':
        game_board['1'] = 'O'
        return game_board
    if random_number == 3 and game_board['3'] == '_':
        game_board['3'] = 'O'
        return game_board

    ## Goes After Middle Move as Fourth Option

    ## Places Randomly Otherwise

    print("_______________________")
    print_board(game_board)


