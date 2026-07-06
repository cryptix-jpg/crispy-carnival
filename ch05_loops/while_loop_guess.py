# DESCRIPTION: Making a program that makes user guess number

def main():

    secretnum = 33
    guess = 0 
    attempts = 0 # counter for guesses

    while guess != secretnum:
        guess = int(input("Guess a number: "))
        attempts += 1

    print(f"You guessed in {attempts} tries.")  # got this to work by pushing it back a line??

main()