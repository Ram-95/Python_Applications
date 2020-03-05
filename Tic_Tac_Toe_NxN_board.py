#Tic Tac Toe - NxN Board. Players will play in turns.

#Random Module to make Computer randomly choose the position to place.
from random import *

def row_check(board, player):
    ''' Checks if all the postions are filled with the player symbol same row-wise. '''
    for i in range(n):
        if board[i].count(player) == n:
            return 1
    return 0


def col_check(board, player):
    ''' Checks if all the postions are filled with the player symbol same column-wise. '''
    for j in range(n):
        if [row[j] for row in board].count(player) == n:
            return 1
    return 0


def diagonal_check(board, player):
    ''' Checks if all the postions are filled with the player symbol diagonally. '''
    #List to store the values for the first(Left to right diagonal) i.e when i == j
    d1 = []
    #List to store the values for the second(Right to left diagonal) i.e when i+j == n-1
    d2 = []
    #Traversing the board and updating the diagonal lists.
    for i in range(n):
        for j in range(n):
            if i == j:
                d1.append(board[i][j])
            elif i+j == n-1:
                d2.append(board[i][j])

    if d1.count(player) == n or d2.count(player) == n:
        return 1
    return 0


def print_board(board):
    ''' Prints the Tic-Tac-Toe Board.'''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end= "   ")
        print(end="\n\n")
    

def winner_check(board, player):
    ''' Checks if there are all same symbols ['X' or 'O'] across diagonals, columns and rows.'''
    if 1 in (row_check(board, player), col_check(board, player), diagonal_check(board, player)):
        return True
    return False



def tic_tac_toe_comp_player(board):
    '''Main Logic of the Game in Computer vs Player Mode. '''
    turns = n*n
    player_name = input('Enter the Name of the Player: ').strip()

    #Visited array to mark as visited
    visited = [x for x in range(turns)]

    #Computer's Symbol
    comp = 'X'
    #Player's Symbol
    player = 'O'

    

    #A NxNtic-tac-toe game will take atmost N^2 moves to know if it was a Tie or not.
    chances = 0

    while True:
        print('-' * string_formatter + ' Computer\'s Turn ' + '-' * string_formatter)
        ch = visited[randrange(0,len(visited))] if len(visited) > 1 else visited[0]
        print('Computer\'s Choice: {}'.format(ch))
        
        #Setting the position given by the Computer with its symbol
        board[d[ch][0]][d[ch][1]] = comp
        visited.remove(ch)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, comp):
            print('Computer Won the Game.')
            return '=' * string_formatter + ' GAME OVER! ' + '=' * string_formatter

        #Break out of the loop when number crosses N^2 {That's when we know if there is a Tie}
        if chances >= turns:
            break
        
    
        print('*' * string_formatter + ' ' + player_name + '\'s Turn ' + '*' * string_formatter)
        
        while True:
            print(visited)
            ch1 = int(input('Choose a position from the above available list: '))
            if ch1 in visited:
                break
            else:
                print('INCORRECT CHOICE!\n')

        #Setting the position given by the user with his symbol
        board[d[ch1][0]][d[ch1][1]] = player
        visited.remove(ch1)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, player):
            print('{} Won the Game.'.format(player_name))
            return '=' * string_formatter + ' GAME OVER! ' + '=' * string_formatter
            
        #Break out of the loop when the number of turns crosses N^2
        if chances >= turns:
            break
        
    return '+' * string_formatter + ' GAME DRAW!!! ' + '+' * string_formatter 




def tic_tac_toe_2_players(board):
    ''' Main Logic of Tic-Tac-Toe Game goes here. Player vs Player Mode. '''
    turns = n*n
    
    first_player_name = input('Enter 1st player name: ').strip()
    second_player_name = input('Enter 2nd player name: ').strip()

    #Visited array to mark as visited
    visited = [x for x in range(turns)]

    #First Player's Symbol
    fp = 'X'
    #Second Player's Symbol
    sp = 'O'

    
    #A NxN tic-tac-toe game will take atmost N^2 moves to know if it was a Tie or not.
    chances = 0

    while True:
        print('*' * string_formatter + ' ' + first_player_name + '\'s Turn ' + '*' * string_formatter)
        
        while True:
            print(visited)
            ch = int(input('Choose a position from the above available list: ')) if len(visited) > 1 else visited[0]
            if ch in visited:
                break
            else:
                print('INCORRECT CHOICE!\n')

        #Setting the position given by the user with his symbol
        board[d[ch][0]][d[ch][1]] = fp
        visited.remove(ch)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, fp):
            print('{} Won the Game.'.format(first_player_name))
            return '=' * string_formatter + ' GAME OVER! ' + '=' * string_formatter

        #Break out of the loop when number crosses N^2 {That's when we know if there is a Tie}
        if chances >= turns:
            break
        
    
        print('*' * string_formatter + ' ' + second_player_name + '\'s Turn ' + '*' * string_formatter)
        
        while True:
            print(visited)
            ch1 = int(input('Choose a position from the above available list: ')) if len(visited) > 1 else visited[0]
            if ch1 in visited:
                break
            else:
                print('INCORRECT CHOICE!\n')

        #Setting the position given by the user with his symbol
        board[d[ch1][0]][d[ch1][1]] = sp
        visited.remove(ch1)
        print('\n')

        #To print board after every move
        print_board(board)
        chances += 1

        #Check if there is a possibility of winning the game
        if winner_check(board, sp):
            print('{} Won the Game.'.format(second_player_name))
            return '=' * string_formatter + ' GAME OVER! ' + '=' * string_formatter
            
        #Break out of the loop when the number of turns crosses N^2
        if chances >= turns:
            break
        
    return '+' * string_formatter + ' GAME DRAW!!! ' + '+' * string_formatter 
        
        
    

''' Driver Code for Tic-Tac-Toe Game. '''
global n
global d

#Global variable used for string formatting - Used in return statements
global string_formatter
string_formatter = 30

#Taking the Board size
n = int(input('Enter the size of the Board{3-10}: '))
if n <= 3:
    n = 3
elif n >= 10:
    n = 10

#Creating a dictionary that maps the positions with the indices of the NxN board.
d = {}
val = 0
for i in range(n):
    for j in range(n):
        d[val] = [i, j]
        val += 1


board = [['_' for i in range(n)] for j in range(n)]
while True:
    option = input('Choose a Game Mode: \n1. Computer vs Player\t\t2. Player vs Player \n')
    if option not in (1, 2, '1', '2'):
        print('Please Choose one of the Two Options.')
    else:
        break

if int(option) == 2:
    print(tic_tac_toe_2_players(board))
elif int(option) == 1:
    print(tic_tac_toe_comp_player(board))
    
