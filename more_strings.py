#!/usr/bin/env/python3

print(f"Splitting s a string on whitespace:")
sentence = input("Please enter a short sentence: ")
sentence = sentence.split()
counter = 1
for word in sentence:
    print(f"Word {counter}: {word} ")
    counter += 1
print()
