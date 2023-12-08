import math
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

    if re.match(r"[A-Z0-9]{3} = \([A-Z0-9]{3}, [A-Z0-90-9]{3}\)", line):
        start, left, right = re.findall(r"([A-Z0-9]{3})", line)
        map[start] = (left, right)
    else:
        directions = line

end = 'ZZZ'

i = 0

nodes = [n for n in map.keys() if n.endswith('A')]
lens = [0]*len(nodes)
for idx, n in enumerate(nodes):
    visited = 0
    curr = n
    while not curr.endswith('Z'):
        l, r = map[curr]
        if directions[i] == 'L':
            curr = l
        else:
            curr = r
        i = (i+1) % len(directions)
        visited += 1
    lens[idx] = visited

lcm = 1
for i in lens:
    lcm = lcm * i // math.gcd(lcm, i)
print(lcm)