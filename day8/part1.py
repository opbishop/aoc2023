import os
import re

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)
directions = []
start = 'AAA'
map = {}
for line in c:
    if line == '':
        continue

    if re.match(r"[A-Z]{3} = \([A-Z]{3}, [A-Z]{3}\)", line):
        start, left, right = re.findall(r"([A-Z]{3})", line)
        map[start] = (left, right)
    else:
        directions = line

end = 'ZZZ'
curr = 'AAA'
i = 0
visited = 0
while curr != end:
    l, r = map[curr]
    if directions[i] == 'L':
        curr = l
    else:
        curr = r
    i = (i+1) % len(directions)
    visited += 1

print(visited)