import random


def display (board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

theboard = ['']*10
###

def player_input():
    enter=''
    while enter !='X' or enter !='Y':
        enter = input("please choose 'x' or 'y ")
    if enter =='X':
        return ('X','Y')
    else:
        return ('Y', 'X')
####
def place_marker(board,marker,position):
    board[position]=marker
##############
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
########
def choose_first():
    person=random.randint(0,1)
    if person==0:
        return 'Player1'
    else:
        return 'Player2'
###############
def space_check(board,position):
    return board[position]==''
##############
def full_check(board,position):
    position=0
    while position not in range(0,11):
        enter1=int(input("please m(0-9"))
    if position in range(0,11):
        return position
#################
def player_choice(board):
    position=int(input("enter a positon"))
    if position in range(0,11):
        return position

##############

def replay():
    choice=input('you wanna play again?')
    return  choice=='yes'

##########

####################
print("welcome to the big game")
gameon=True
while True:
    display(theboard)
    player1marker,player2marker=player_input()
    turn=choose_first()
    while gameon:
        if turn=='player1':
            position=player_choice(theboard)


            marked=place_marker(theboard,player1marker,position)
            if win_check(theboard,player1marker):
                gameon=False

            else:
                if full_check(theboard,position):
                    display("tie")
                else:
                    turn='Player2'




        else:
            turn=='Player2'
            position = player_choice(theboard)

            marked = place_marker(theboard, player2marker, position)
            if win_check(theboard, player2marker):
                gameon = False

            else:
                if full_check(theboard, position):
                    display("tie")
                else:
                    turn = 'Player1'






    if replay()=='yes':
        break