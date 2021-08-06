#!/usr/bin/env/python3

print()
name = input('Please enter your name: ')
name = name.strip()
age = int(input('Please enter your age: '))


message = f"Your name is {name} and your age is {age}"
print(message)
print('-----------')
print()

data = ['water', 'tacos', 'french fries', 'pizza']
for i in data:
    print(i, sep = "", end = ' ')
print()
print('-----------')
print()

number_list = []
num_count = 0
sum = 0
done = False
while not done:
    num = int(input('Please enter a number: '))
    number_list.append(num)
    sum += num
    num_count += 1
    response = input('Enter another number (Y/n)? ')
    if response.upper() != 'Y':
        done = True

print()
print('------------------')
print(f"Numbers entered: {num_count}")
print(f"Sum: {sum}")
print(f"Average: {sum / num_count}")
print('------------------')
print()

