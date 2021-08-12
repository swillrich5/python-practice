import csv

FILENAME='marvel_characters.csv'

character_list = []
character_name = ""
secret_identity = ""

def write_characters(character_list):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(character_list)

def add_character(name, identity):
        marvel_character = [name, identity]
        character_list.append(marvel_character)

def main():
    done = False
    while not done:
        character_name = input('Please enter a Marvel character\'s name: ')
        secret_identity = input('Please enter the character\'s secret identity: ')
        add_character(character_name, secret_identity)
        another_character = input('Would you like to enter another character? (y/n): ')
        if another_character.lower() != 'y':
            done = True
    write_characters(character_list)

if __name__ == "__main__":
    main()