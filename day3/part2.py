import collections
import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

i = 0
nums_near_symbols = collections.defaultdict(list)


def is_near_symbol(i, j, c):
    non_symbols = ('.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    for coord in (
            (i - 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i, j - 1),
            (i, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
            (i + 1, j + 1)
    ):
        try:
            if c[coord[0]][coord[1]] not in non_symbols:
                return coord
        except IndexError:
            continue


while i < len(c):
    row = c[i]
    j = 0
    while j < len(row):
        char = row[j]
        near_symbols = set()
        if char.isnumeric():
            if sym := is_near_symbol(i, j, c):
                near_symbols.add(sym)
            nums = []
            nums.append(char)
            nextcharindex = j + 1
            while nextcharindex < len(row) and row[nextcharindex].isnumeric():
                if sym := is_near_symbol(i, nextcharindex, c):
                    counted = True
                    near_symbols.add(sym)
                nums.append(row[nextcharindex])
                nextcharindex += 1
            j = nextcharindex - 1
            if len(near_symbols) != 0:
                for sym in near_symbols:
                    nums_near_symbols[sym].append(int(''.join(nums)))

        j += 1
    i += 1

s = 0
for sym, nums in nums_near_symbols.items():
    if len(nums) == 2:
        ratio = nums[0] * nums[1]
        s += ratio

print(s)
