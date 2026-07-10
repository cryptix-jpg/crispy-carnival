# DESCRIPTION: utilities for fortune_machine.py

import random

fortunes = [
            'You will live a long, prosperous life.\n',
            'Bring an umbrella today.\n',
            'Fear is for chumps!\n',
            'If you have no pockets, your phone can\'t fall out of them!\n',
            'Yoda was wrong. "Trying" is a thing.\n',
            'There\'s a lot of atoms in you.\n',
            'Chin up! It\'s going to be a great day!\n'
            ]

def get_directions():
    print()
    dashes()
    print('Welcome to the Fortune Telling Machine')
    print()
    print('The instructions are simple - you may request one')
    print('fortune, you  may request multiple fortunes, or you')
    print('may request to quit.')
    print()
    print('Please enjoy your fortune(s)! But beware! When you use')
    print('the Fortune Telling Machine, you get what you get and')
    print('you don\'t get upset!')
    print()

def get_one_fortune():
    print(random.choice(fortunes))
    print()

def get_multiple_fortunes(number_of_fortunes):
    print()
    for x in range(number_of_fortunes):
        print((x + 1),'-',random.choice(fortunes))

def dashes():
    print('--------------------------------------------------')

def quit():
    print()
    print('I hope you enjoyed your fortunes...')