# DESCRIPTION: this one is for fun, put your dogs in and get a good doggo
# user must type 'DONE' to end 


def main():
    doggo_names = get_doggo_names()
    output_names(doggo_names)

def get_doggo_names():
    name = ''
    names = []
    while name != 'DONE':
        name = input('Name of doggo: ')
        if name != 'DONE':
            names.append(name)
    
    return names

def output_names(doggo_names):

    for name in doggo_names:
        print(f"{name} is awesome.")

    

main()