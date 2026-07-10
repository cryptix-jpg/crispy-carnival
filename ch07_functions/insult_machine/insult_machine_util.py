# DESCRIPTION: the utils for insult_machine.py as well as messing with docstring

import random

insults = [
    'You look like a bunch of rocks',
    'AHHH',
    'this is the second insult',
    'this is the third insult',
    'this is the fourth insult',
    'this is the fifth isult'
]

def welcome():
    print("---------------------------------")
    print("Welcome to the Insulternator 3500")
    print("---------------------------------")
    print("")
    '''
    This function should output four lines (three lines of text as described in the SAMPLE OUTPUT and one blank line).
    '''    


def show_all_insults():
    print(insults)
    '''
    This function simply outputs the values in the list called 'insults'.
    '''


def one_insult():
    print(random.choice(insults))
    '''
    This function will print one insult from the list at random using `random.choice()`.
    '''

    
def two_insults():
    one_insult()
    one_insult
    '''
    This function will print two insults from the list at random. NEEDS to call `one_insult()` twice.
    '''


def insult_specific_name(name):
    # one_insult() 
    print(f"{name}, here is your insult: ", random.choice(insults))
    '''
    This function takes in a name from the main program and then will personlize an insult chosen at random from the list.
    '''


def insult_x_number_of_insults(num):
    for x in range(num):
        print(random.choice(insults))
    '''
    This function takes in one variable, `num`, and will dispense that number of insults at random from the list.
    '''


def goodbye():
    print("")
    print("---------------------------------------------")
    print("Thank you for playing the Insulternator 3500!")
    print("---------------------------------------------")
    '''
    This function should output four lines (one blank line and three lines of text as described in the SAMPLE OUTPUT).
    '''    