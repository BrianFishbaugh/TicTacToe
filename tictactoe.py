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

def computer_play(game_board):
    print_board(game_board)
    
    random_number = random.randint(0, 3) 

                        ######## Goes After Winning Move First ########
    #Across the Top
    if game_board['7'] == game_board['8'] and game_board['9'] == '_' and game_board['7'] == 'O':
        game_board['9'] == 'O'
        return game_board
    if game_board['7'] == game_board['9'] and game_board['8'] == '_' and game_board['7'] == 'O':
        game_board['8'] == 'O'
        return game_board
    if game_board['8'] == game_board['9'] and game_board['7'] == '_' and game_board['8'] == 'O':
        game_board['7'] == 'O'
        return game_board

    #Across the Middle
    if game_board['4'] == game_board['5'] and game_board['6'] == '_' and game_board['4'] == 'O':
        game_board['6'] == 'O'
        return game_board
    if game_board['4'] == game_board['6'] and game_board['5'] == '_' and game_board['4'] == 'O':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['6'] and game_board['4'] == '_' and game_board['5'] == 'O':
        game_board['4'] == 'O'
        return game_board

    #Across The Bottom
    if game_board['1'] == game_board['2'] and game_board['3'] == '_' and game_board['1'] == 'O':
        game_board['3'] == 'O'
        return game_board
    if game_board['1'] == game_board['3'] and game_board['2'] == '_' and game_board['1'] == 'O':
        game_board['2'] == 'O'
        return game_board
    if game_board['2'] == game_board['3'] and game_board['1'] == '_' and game_board['2'] == 'O':
        game_board['1'] == 'O'
        return game_board

    #Left Column
    if game_board['7'] == game_board['4'] and game_board['1'] == '_' and game_board['7'] == 'O':
        game_board['1'] == 'O'
        return game_board
    if game_board['7'] == game_board['1'] and game_board['4'] == '_' and game_board['7'] == 'O':
        game_board['4'] == 'O'
        return game_board
    if game_board['4'] == game_board['1'] and game_board['7'] == '_' and game_board['4'] == 'O':
        game_board['7'] == 'O'
        return game_board

    #Middle Colum
    if game_board['8'] == game_board['5'] and game_board['2'] == '_' and game_board['8'] == 'O':
        game_board['2'] == 'O'
        return game_board
    if game_board['8'] == game_board['2'] and game_board['5'] == '_' and game_board['8'] == 'O':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['2'] and game_board['8'] == '_' and game_board['5'] == 'O':
        game_board['8'] == 'O'
        return game_board

    #Right Column
    if game_board['9'] == game_board['6'] and game_board['3'] == '_' and game_board['9'] == 'O':
        game_board['3'] == 'O'
        return game_board
    if game_board['9'] == game_board['3'] and game_board['6'] == '_' and game_board['9'] == 'O':
        game_board['6'] == 'O'
        return game_board
    if game_board['6'] == game_board['3'] and game_board['9'] == '_' and game_board['6'] == 'O':
        game_board['9'] == 'O'
        return game_board

    #Left to Right Diaganal
    if game_board['7'] == game_board['5'] and game_board['3'] == '_' and game_board['7'] == 'O':
        game_board['3'] == 'O'
        return game_board
    if game_board['7'] == game_board['3'] and game_board['5'] == '_' and game_board['7'] == 'O':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['3'] and game_board['7'] == '_' and game_board['5'] == 'O':
        game_board['7'] == 'O'
        return game_board

    #Right to Left Diagonal
    if game_board['9'] == game_board['5'] and game_board['1'] == '_' and game_board['9'] == 'O':
        game_board['1'] == 'O'
        return game_board
    if game_board['9'] == game_board['1'] and game_board['5'] == '_' and game_board['9'] == 'O':
        game_board['8'] == 'O'
        return game_board
    if game_board['5'] == game_board['1'] and game_board['9'] == '_' and game_board['5'] == 'O':
        game_board['9'] == 'O'
        return game_board
    

    ########## Blocks Winning Move Second #########
    if game_board['7'] == game_board['8'] and game_board['9'] == '_' and game_board['7'] == 'X':
        game_board['9'] == 'O'
        return game_board
    if game_board['7'] == game_board['9'] and game_board['8'] == '_' and game_board['7'] == 'X':
        game_board['8'] == 'O'
        return game_board
    if game_board['8'] == game_board['9'] and game_board['7'] == '_' and game_board['8'] == 'X':
        game_board['7'] == 'O'
        return game_board

    #Across the Middle
    if game_board['4'] == game_board['5'] and game_board['6'] == '_' and game_board['4'] == 'X':
        game_board['6'] == 'O'
        return game_board
    if game_board['4'] == game_board['6'] and game_board['5'] == '_' and game_board['4'] == 'X':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['6'] and game_board['4'] == '_' and game_board['5'] == 'X':
        game_board['4'] == 'O'
        return game_board

    #Across The Bottom
    if game_board['1'] == game_board['2'] and game_board['3'] == '_' and game_board['1'] == 'X':
        game_board['3'] == 'O'
        return game_board
    if game_board['1'] == game_board['3'] and game_board['2'] == '_' and game_board['1'] == 'X':
        game_board['2'] == 'O'
        return game_board
    if game_board['2'] == game_board['3'] and game_board['1'] == '_' and game_board['2'] == 'X':
        game_board['1'] == 'O'
        return game_board

    #Left Column
    if game_board['7'] == game_board['4'] and game_board['1'] == '_' and game_board['7'] == 'X':
        game_board['1'] == 'O'
        return game_board
    if game_board['7'] == game_board['1'] and game_board['4'] == '_' and game_board['7'] == 'X':
        game_board['4'] == 'O'
        return game_board
    if game_board['4'] == game_board['1'] and game_board['7'] == '_' and game_board['4'] == 'X':
        game_board['7'] == 'O'
        return game_board

    #Middle Colum
    if game_board['8'] == game_board['5'] and game_board['2'] == '_' and game_board['8'] == 'X':
        game_board['2'] == 'O'
        return game_board
    if game_board['8'] == game_board['2'] and game_board['5'] == '_' and game_board['8'] == 'X':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['2'] and game_board['8'] == '_' and game_board['5'] == 'X':
        game_board['8'] == 'O'
        return game_board

    #Right Column
    if game_board['9'] == game_board['6'] and game_board['3'] == '_' and game_board['9'] == 'X':
        game_board['3'] == 'O'
        return game_board
    if game_board['9'] == game_board['3'] and game_board['6'] == '_' and game_board['9'] == 'X':
        game_board['6'] == 'O'
        return game_board
    if game_board['6'] == game_board['3'] and game_board['9'] == '_' and game_board['6'] == 'X':
        game_board['9'] == 'O'
        return game_board

    #Left to Right Diaganal
    if game_board['7'] == game_board['5'] and game_board['3'] == '_' and game_board['7'] == 'X':
        game_board['3'] == 'O'
        return game_board
    if game_board['7'] == game_board['3'] and game_board['5'] == '_' and game_board['7'] == 'X':
        game_board['5'] == 'O'
        return game_board
    if game_board['5'] == game_board['3'] and game_board['7'] == '_' and game_board['5'] == 'X':
        game_board['7'] == 'O'
        return game_board

    #Right to Left Diagonal
    if game_board['9'] == game_board['5'] and game_board['1'] == '_' and game_board['9'] == 'X':
        game_board['1'] == 'O'
        return game_board
    if game_board['9'] == game_board['1'] and game_board['5'] == '_' and game_board['9'] == 'X':
        game_board['8'] == 'O'
        return game_board
    if game_board['5'] == game_board['1'] and game_board['9'] == '_' and game_board['5'] == 'X':
        game_board['9'] == 'O'
        return game_board

    ##### Goes After Corner Slots if Open and No winning / Stop From Winning turns are available
    if random_number == 0 and game_board['7'] == '_' :
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

    ###### Goes After Middle Move as Fourth Option ########
    if game_board['7'] != '_' and game_board['9'] != '_' and game_board['1'] != '_' and game_board['3'] != '_':
        game_board['5'] = 'O'
        return game_board

    ## Places Randomly Otherwise
    if random_number == 0 and game_board['8'] == '_' :
        game_board['8'] = 'O'
        return game_board
    if random_number == 1 and game_board['4'] == '_':
        game_board['4'] = 'O'
        return game_board
    if random_number == 2 and game_board['6'] == '_':
        game_board['6'] = 'O'
        return game_board
    if random_number == 3 and game_board['2'] == '_':
        game_board['2'] = 'O'
        return game_board

def player_turn(game_board): 
    z = True
    while z == True:
        print("Where Do you Want to Place Your Letter?")
        player_input = input()

        if game_board.get(player_input) == None:
            print("Invalid Option")
            z == True

        else:
            game_board[player_input] = 'X'
            print_board(game_board)
            return game_board
            z = False

player_turn(game_board)

