import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

nums = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

total_sum = 0
first_chars = [c[0] for c in nums.keys()]
last_chars = [c[-1] for c in nums.keys()]

for line in c:
    first = None
    i = 0
    while i < len(line):
        if line[i] in first_chars:
            found = False
            for k in nums.keys():
                if line[i:i+len(k)] == k:
                    first = nums[k]
                    found = True
                    break
            if found:
                break
        elif line[i].isnumeric():
            first = line[i]
            break
        i += 1
    j = len(line) -1
    last = None
    while j >= 0:
        if line[j] in last_chars:
            found = False
            for k in nums.keys():
                if line[j-len(k)+1:j+1] == k:
                    last = nums[k]
                    found = True
                    break
            if found:
                break
        elif line[j].isnumeric():
            last = line[j]
            break
        j -= 1

    s = f"{first}{last}"
    print(f"{line} - {s}")
    total_sum += int(s)

print(total_sum)