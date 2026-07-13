# DESCRIPTION : my midterm project


results = []

print("Welcome to the Mathenator2000")

play_again = 'y'
while play_again == 'y':
    print("")
    print("Please choose from the following menu:")
    print("  1. Compute area of a circle")
    print("  2. Compute area of a rectangle")
    print("")
    user_choice = int(input("What is your choice? "))
    print("")

    if user_choice == 1: 
        radius = float(input("What is the radius of the circle? "))
        area_choice_one = 3.14 * radius **2
        print(f"The area of the circle is {area_choice_one}")
        results.append(f"The area of the circle is {area_choice_one}")
    elif user_choice == 2:
        length_of = float(input("What is the length of the rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area_choice_two = length_of * width
        print(f"The area of the rectangle is {area_choice_two}")
        results.append(f"The area of the rectangle is {area_choice_two}")
    else:
        print("Invalid selection.")
    print("")
    play_again = input("Would you like to play again (y/n)? ")
print("")
print("-------------------------")
print("A record of your results: ")
print(results)
print("")
print("Thank you for using the Mathenator2000")