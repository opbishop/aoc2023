import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)
s = 0

for card in c:
    winning, have = card.split('|')
    winning = winning.split(':')[1].split(' ')
    have = [x.strip() for x in have.split(' ') if x.isnumeric()]
    winning = [x for x in winning if x.isnumeric()]

    have = set(have)
    winning = set(winning)

    matches = have.intersection(winning)

    if len(matches) > 0:
        points = 2**(len(matches) -1)
        s += points

print(s)
