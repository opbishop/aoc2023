import os

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

total_count = {
    'red': 12,
    'green': 13,
    'blue': 14
}

s = 0

for line in c:
    g = int(line.split(':')[0].split(' ')[1])
    games = line.split(':')[1].split(';')
    invalid = False

    for game in games:
        if invalid:
            break
        for i in game.split(','):
            i = i.strip()
            count, colour = i.split(' ')
            if int(count) > total_count[colour]:
                print(f"Game {g} invalid because {count} > {total_count[colour]}")
                invalid = True
                break

    if not invalid:
        s += g

print(s)