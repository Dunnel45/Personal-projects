#!/usr/bin/env python3

import random
import sys

number = random.randint(1, 10)
tries = 1


uname = input('Hello, please enter your name! ')

print('Hello', uname + '.')

question = input('Do you want to play? [Y/N] ')
if question == 'n':
    print('Thanks for joining')

if question == 'y':
    print('I am thinking of a number between 1 and 10')
    guess = int(input('Have a guess: '))
    while guess != number:
        tries += 1
        guess = int(input('Oops, try again: '))

        if guess > number:
            print('Too high, guess lower')

        if guess < number:
            print('Too low, guess higher')

        if guess == number:
            print('Well done!! you guessed right. The number was {}, it took you {} tries'.format(number, tries))
