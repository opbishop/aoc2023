import math
import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

powers = []

for line in c:
    g = int(line.split(':')[0].split(' ')[1])
    games = line.split(':')[1].split(';')
    invalid = False
    minima = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for game in games:
        if invalid:
            break
        for i in game.split(','):
            i = i.strip()
            count, colour = i.split(' ')
            minima[colour] = max(minima[colour], int(count))
    powers.append(math.prod(minima.values()))

print(sum(powers))
