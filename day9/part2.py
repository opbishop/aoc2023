import os
import re

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

vals = []
for line in c:
    nums = [int(i) for i in re.findall(r"-{0,1}\d+", line)]
    stack = []
    stack.append(nums)

    while not all(x == 0 for x in stack[-1]):
        n = stack[-1]
        diffs = []
        i = 0
        while i < len(n) - 1:
            diffs.append(n[i + 1] - n[i])
            i += 1
        stack.append(diffs)

    for i in range(len(stack)-1, -1, -1):
        if i == len(stack) -1:
            stack[i].insert(0, 0)
        else:
            stack[i].insert(0, (stack[i][0] - stack[i+1][0]))

    vals.append(stack[0][0])

print(sum(vals))
