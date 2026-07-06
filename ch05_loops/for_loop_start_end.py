# DESCRIPTION:  Asking user for a starting number and ending number and then displaying all numbers

start = int(input("Starting point: "))
end = int(input("Ending point: "))

def main():
    for x in range(start, end + 1):
        print(x)

main()