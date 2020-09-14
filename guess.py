#!/usr/bin/env python3

import random
from num2words import num2words
from subprocess import call

import sys

cmd_beg= 'espeak -s 100 -v other/en-sc '
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the s$

#Calls the Espeak TTS Engine to read aloud a Text
#call([cmd_beg+text+cmd_end], shell=True)


number = random.randint(1, 10)
tries = 1

text = 'Hello sir or madam, please enter your name and have fun'
text = text.replace(' ','_')
call([cmd_beg+text+cmd_end], shell=True)

uname = input('Hello, please enter your name! ')

text = "Hello " + uname
text = text.replace(' ','_')
call([cmd_beg+text+cmd_end], shell=True)
#print('Hello', uname + '.')

text = "Do you want to play" + uname + "enter y for yes and n for no "
text = text.replace(' ','_')
call([cmd_beg+text+cmd_end], shell=True)

question = input('Do you want to play? [Y/N] ')
if question == 'n':
    print("Goodbye!!")
    text = 'Thanks for joining'
    text = text.replace(' ','_')
    call([cmd_beg+text+cmd_end], shell=True)

if question == 'y':
    text = 'I am thinking of a number between 1 and 10'
    text = text.replace(' ','_')
    call([cmd_beg+text+cmd_end], shell=True)
    guess = int(input('Have a guess: '))
    while guess != number:
        tries += 1
        text = 'Sorry idiot try again'
        text = text.replace(' ','_')
        call([cmd_beg+text+cmd_end], shell=True)
        guess = int(input("go again: "))

        if guess > number:
            print("too high")
            text = 'Wrong dummy too high, guess lower'
            text = text.replace(' ','_')
            call([cmd_beg+text+cmd_end], shell=True)

        if guess < number:
            print("too low")
            text = 'Wrong dummy too low, guess higher'
            text = text.replace(' ','_')
            call([cmd_beg+text+cmd_end], shell=True)
            #print('Too low, guess higher')

        if guess == number:
            "correct!!!"
            text = 'Well done you guessed right The number was {}, it took you {} tries'.format(number, tries)
            text = text.replace(' ','_')
            call([cmd_beg+text+cmd_end], shell=True)