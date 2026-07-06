# DESCRIPTION:  Making a password authenticator 

def main(): 
    password = "tooManySecrets" # tooManySecrets is the password ;)
    attempts = ""

    while attempts != password: # this allows attempts until guessed!
        attempts = input('Enter password: ')
        if attempts == password:
            print(" ")
            print("Access granted.")
        else:
            print(" ")
            print("Password does not match.")


main()