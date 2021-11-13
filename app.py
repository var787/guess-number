# Guess the number
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
          guess = int(input(f'Guess a number between 1 & {x}:'))
          if  random_number > guess:
            print('Sorry, too low')
          elif random_number < guess:
            print('Sorry, too high')
    print(f'Yay!!, you guessed the right number {random_number}')



guess(10)