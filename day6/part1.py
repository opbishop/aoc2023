import math
import os
import re

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

times = [int(i) for i in re.findall(r"\d+", c[0])]
dists = [int(i) for i in re.findall(r"\d+", c[1])]

results = []
speed_prod = []

for race in range(len(times)):
    valid_speeds = 0
    speed = dists[race]
    while speed > 0:
        time_left = times[race] - speed
        if (time_left * speed) > dists[race]:
            valid_speeds += 1
        speed -= 1
    speed_prod.append(valid_speeds)

print(math.prod(speed_prod))