# DESCRIPTION: Using fortune util practice functions

import fortune_util

def main():
    run_fortune_machine()

def run_fortune_machine():

    fortune_util.get_directions()
    fortune_util.dashes()
    print("ONE FORTUNE:")
    fortune_util.get_one_fortune()
    fortune_util.dashes()
    print("MULTIPLE FORTUNES:")
    many_fortunes = int(input("How many fortunes would you like? "))
    fortune_util.get_multiple_fortunes(many_fortunes)
    fortune_util.dashes()
    fortune_util.quit()


main()