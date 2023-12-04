import collections
import os

from common.common import get_input
import time

t = time.time()
cwd = os.getcwd()
c = get_input(cwd)
s = 0

card_points = [0] * len(c)

duplicate_cards = collections.defaultdict(int)

for card in c:
    winning, have = card.split('|')
    card = int(winning.split(':')[0].split()[1])
    winning = winning.split(':')[1].split(' ')
    have = [x.strip() for x in have.split(' ') if x.isnumeric()]
    winning = [x for x in winning if x.isnumeric()]

    have = set(have)
    winning = set(winning)

    matches = have.intersection(winning)

    for _ in range(duplicate_cards[card] +1):
        if len(matches) > 0:
            for i in range(len(matches)):
                duplicate_cards[card+i+1] += 1

    s += duplicate_cards[card] +1

print(s)
print(f"{time.time() -t}")