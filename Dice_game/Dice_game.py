# Dice Game between 2 Players
# The winner will be the first player to score a 36.


from random import randint
import time
import sys
print('Welcome to Dice Game\n---------------------------------------------')
player1 = input('Enter the 1st player name: ').strip()
player2 = input('Enter the 2nd player name: ').strip()
print('{} -> 1st Player\n{} -> 2nd Player'.format(player1, player2))

#this is to choose the next player 0 - first player 1- second player
chance = 0      

#tries - 1st player  tries1 - 2nd player
(tries,tries1) = (0,0)

#Total scores of players
(total, total1) = (0,0)

max_score = 36
DECORATE_COUNT = 45

# Iterate until a player is won
while(1):
    print(f'\nScores: ')
    print('='*DECORATE_COUNT)
    print(f'{player1}: {total}\n{player2}: {total1}')
    print('='*DECORATE_COUNT)
    #1st player chance
    while(chance == 0):     
        print('\n')
        print('{}(1st Player\'s) Chance.. '.format(player1))
        print('-----------------------------------------------')
        roll = input('Roll Dice! Press 1 to roll: ').strip()
        if roll in (1,'1'):
            dice = randint(1,6)
            total = total + dice
            tries = tries + 1
            print('{}(1st Player) rolled a {} and total is {}'.format(player1, dice, total))
        else:
            print('\nINCORRECT KEY PRESSED.PRESS 1 TO ROLL DICE.')
            continue
        #giving chance to 2nd player
        chance = 1      

        if total >= max_score:
            print('\n\n******************* GAME OVER ********************\n')
            print('\n{}(Player1) Won the Game in {} tries. Congratulations!!!'.format(player1, tries))
            sys.exit()

    #2nd player chance
    while(chance == 1):     
        print('\n')
        print('{}(2nd Player\'s) Chance.. '.format(player2))
        print('*************************************************')
        roll = input('Roll Dice! Press 1 to roll: ').strip()
        if roll in (1, '1'):
            dice = randint(1,6)
            total1 = total1 + dice
            tries1 = tries1 + 1
            print('{}(2nd Player) rolled a {} and total is {}'.format(player2, dice, total1))
        else:
            print('\nINCORRECT KEY PRESSED.PRESS 1 TO ROLL DICE.')
            continue

        #giving chance to 1st player
        chance = 0      

        if total1 >= max_score:
            print('\n\n******************* GAME OVER ********************\n')
            print('{}(Player1) won the Game in {} tries. Congratulations!!!\n'.format(player2, tries1))
            sys.exit()
