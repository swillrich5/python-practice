#!/usr/bin/env/python3
num_lines = 0
char_count = 0
with open('file_to_read.txt') as file:
    for line in file:
        num_lines += 1
        line = line.replace("\n", "")
        for ch in line:
            char_count += 1
        print(line)

print()
print(" ----- Analysis of File Text ----- ")
print(f"Number of lines in file: {num_lines}")
print(f"Number of characters in file: {char_count}")
print()

