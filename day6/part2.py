import math
import os
import re

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

times = [int(i) for i in re.findall(r"\d+", c[0].replace(' ', ''))]
dists = [int(i) for i in re.findall(r"\d+", c[1].replace(' ', ''))]

results = []

for race in range(len(times)):
    a = 1
    b = times[race] * -1
    c = dists[race] + 1

    y = math.sqrt((b**2) - 4*(a*c))

    min_speed = ((b*-1) - y) / 2*a
    max_speed = ((b*-1) + y) / 2*a

    print(f"{int(max_speed) - int(math.ceil(min_speed)) + 1}")
