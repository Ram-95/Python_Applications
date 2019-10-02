#Tic Tac Toe - Basic 3x3 Board. Players will play in turns.

from random import *




def row_check(board, player):
    for i in range(3):
        if (board[i][0] == player) and (board[i][1] == player) and (board[i][2] == player):
            return 1
    return 0


def col_check(board, player):
    for j in range(3):
        if (board[0][j] == player) and (board[1][j] == player) and (board[2][j] == player):
            return 1
    return 0


def diagonal_check(board, player):
    if ((board[0][0] == player) and (board[1][1] == player) and (board[2][2] == player)) or ((board[0][2] == player) and (board[1][1] == player) and (board[2][0] == player)):
        return 1
    return 0


def print_board(board):
    ''' Prints the Tic-Tac-Toe Board.'''
    for i in range(3):
        for j in range(3):
            print(board[i][j], end= "   ")
        print(end="\n\n")
    

def winner_check(board, player):
    ''' Checks if there are all 'player'['X' or 'O'] across diagonals, columns and rows.'''
    if 1 in (row_check(board, player), col_check(board, player), diagonal_check(board, player)):
        return True
    return False
    
   

def tic_tac_toe_2_players(board):
    #Visited array to mark as visited
    turns = 9
    win_flag = 0
    visited = [x for x in range(turns)]
    fp = 'X'
    sp = 'O'
    d = {0 :[0,0], 1: [0,1], 2: [0,2], 3: [1,0], 4: [1,1], 5: [1,2], 6: [2,0], 7: [2,1], 8: [2,2]}

    chances = 0

    while True:
        print('------------------------------ First Player Turn --------------------------------')
        print(visited)
        ch = int(input('Choose a position from the above available list: '))
        board[d[ch][0]][d[ch][1]] = fp
        visited.remove(ch)
        print('\n')
        print_board(board)
        chances += 1

        if winner_check(board, fp):
            print('First Player Won the Game.')
            win_flag = 1
            return '=========================== Game Over! ============================'
            
        if chances >= 9:
            break
        
    
        print('****************************** Second Player Turn *********************************')
        print(visited)
        ch1 = int(input('Choose a position from the above available list: '))
        board[d[ch1][0]][d[ch1][1]] = sp
        visited.remove(ch1)
        print('\n')
        print_board(board)
        chances += 1

        if winner_check(board, sp):
            print('Second Player Won the Game.')
            win_flag = 1
            return '=========================== Game Over! ============================'
            

        if chances >= 9:
            break
        print('Chances: {}'.format(chances))
    return '++++++++++++ Draw Game!!! +++++++++++++++++' 
        
        
    


board = [['_' for i in range(3)] for j in range(3)]
print_board(board)
print(tic_tac_toe_2_players(board))








'''
-- First player is 'X' and the other is 'O'.
-- User Should give a number [0-8] that denotes the cell number.
-- Maintain a visited array [0-8] and mark it as visited, for all the numbers that the players had chosen earlier
   such that already existing 'O' and 'X' are not altered.



1. Two Modes --> Computer vs Player and Player1 vs player2
2. For Computer, use random module and place either 'O' or 'X' at a random AVAILABLE position.
3. For Two Players, make turns and take their input.
4. Print the Board after every turn.


5. Extend the game to more than 3x3 board i.e, write code for tic-tac-toe on a NxN board.
'''
