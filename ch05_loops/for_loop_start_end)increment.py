# DESCRIPTION: number has a start end and increment !

startin = int(input("Starting point: "))
endin = int(input("Ending point: "))
incre = int(input("Increment by: "))

def main():
    for number in range(startin, endin, incre):
        print(number, end=' ')

main()

# sample output vvv 
'''
Starting point: 3
Ending point: 12
Increment by: 4
3 7 11 
'''