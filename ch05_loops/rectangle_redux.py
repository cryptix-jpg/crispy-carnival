# DESCRIPTION:  Users get to make a rectangle but cooler

def main():\

    tall = int(input("How tall would you like the rectangle? "))
    stars = "*   *"
    
    print("*****")      # top of the rectangle
    count = 0           # this variable is to stop an infinite loop
    while count < tall:
        print(stars)
        count += 1      # loop stops because count is not = 0 anymore it is 1
    print("*****")      # bottom of the rectangle

main()