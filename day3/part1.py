import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

i = 0


def is_near_symbol(i, j, c):
    non_symbols = ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for coord in (
            (i-1, j),
            (i-1, j-1),
            (i-1, j+1),
            (i, j-1),
            (i, j+1),
            (i+1, j),
                (i+1, j-1),
            (i+1, j+1)
    ):
        try:
            if c[coord[0]][coord[1]] not in non_symbols:
                return True
        except IndexError:
            continue

s = 0

while i < len(c):
    row = c[i]
    j = 0
    while j < len(row):
        char = row[j]
        counted = False
        if char.isnumeric():
            if is_near_symbol(i, j, c):
                counted = True
            nums = []
            nums.append(char)
            nextcharindex = j+1
            while nextcharindex < len(row) and row[nextcharindex].isnumeric():
                if not counted and is_near_symbol(i, nextcharindex, c):
                    counted = True
                nums.append(row[nextcharindex])
                nextcharindex += 1
            j = nextcharindex - 1
            if counted:
                n = ''.join(nums)
                print(n)
                s += int(n)
        j += 1
    i += 1

print(s)