#!/usr/bin/env/python3
num_lines = 0
char_count = 0
file_read_buffer = []
with open('file_to_read.txt') as file:
    for line in file:
        num_lines += 1
        line = line.replace("\n", "")
        for ch in line:
            char_count += 1
        file_read_buffer.append(line)
        print(line)

print()
print(" ----- Analysis of File Text ----- ")
print(f"Number of lines in file: {num_lines}")
print(f"Number of characters in file: {char_count}")
print()
print(' ----- Contents of file_read_buffer ----- ')
print(file_read_buffer)

with open('file_to_write.txt', "w") as file:
    for line in file_read_buffer:
        file.write(line + "\n")

