#!/usr/bin/env/python3
print(' ---------------------------------- ')
print(f"Splitting s a string on whitespace:")
print(' ---------------------------------- ')
sentence = input("Please enter a short sentence: ")
sentence = sentence.split()
counter = 1
for word in sentence:
    print(f"Word {counter}: {word} ")
    counter += 1
print(' ---------------------------------- ')
print()

print(' ---------------------------------- ')
print(f"Splitting s a date on delimiter:")
print(' ---------------------------------- ')
date = input("Please enter a date using / as a delimiter (MM/DD/YYYY): ")
date = date.split("/")
print(f"Month: {date[0]}")
print(f"Day: {date[1]}")
print(f"Year: {date[2]}")
print(' ---------------------------------- ')
print()
