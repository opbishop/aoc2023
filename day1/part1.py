import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

total_sum = 0

for line in c:
    first = None
    last = None
    for char in line:
        if char.isnumeric():
            first = char
            break
    for char in reversed(line):
        if char.isnumeric():
            last = char
            break
    s = first + last
    total_sum += int(s)

print(total_sum)