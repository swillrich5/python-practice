#!/usr/bin/env/python3

import random

num_list = [5, 43, 34, 98, 22, 133, 72, 55]

print()
print('------------------')
print(f"Our number list: {num_list}")
print(f"Number of elements in list: {len(num_list)}")
print(f"Our number list sorted: {sorted(num_list)}")
reversed_num_list = list(reversed(num_list))
print(f"Our number list reversed: {reversed_num_list}")

print(f"The sum() built-in function returns: {sum(num_list)}")
print(f"Our number list's minimum value: {min(num_list)}")
print(f"Our number list's maximum value: {max(num_list)}")
print(f"A random number from the list: {random.choice(num_list)}")
random.shuffle(num_list)
print(f"Our number list shuffled: {num_list}")
print('------------------')
print()