import csv

FILENAME='marvel_characters.csv'

character_list = []
character_name = ""
secret_identity = ""

def add_character(name, identity):
    character_list.append([name, identity])

def main():
    done = False
    while not done:
        character_name = input('Please enter a Marvel character\'s name: ')
        secret_identity = input('Please enter the character\'s secret identity: ')
        add_character(character_name, secret_identity)
        another_character = input('Would you like to enter another character? (y/n): ')
        if another_character.lower() != 'y':
            done = True
    print(character_list)

if __name__ == "__main__":
    main()