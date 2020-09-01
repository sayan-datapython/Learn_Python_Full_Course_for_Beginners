import random

player = int(input('Enter any number between 1 to 5: '))

if player == random.randint(0,5):
    print('Your Win, right number {}'.format(player))
else:
    print('Not the number, PC win {}'.format(player))
