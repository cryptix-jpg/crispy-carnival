# DESCRIPTION: Making a hot-cold number guesser and attemps are counted

def main():
    secretnum = 33  # this is the very super secret number
    guess = 0
    attempts = 0

    while guess != secretnum:
        guess = int(input("Guess a number: "))
        attempts += 1

        if guess < secretnum:
            print("Your guess is too low.")
            print(" ")
        elif guess > secretnum:
            print("Your guess is too high.")
            print(" ")


        
    print("")
    print(f"You guessed in {attempts} tries.")
main()