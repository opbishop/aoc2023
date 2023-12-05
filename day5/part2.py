import math
import os
import re
from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

seed_pairs = []
for pair in re.findall(r"\d+ \d+", c[0]):
    start, l = pair.split()
    seed_pairs.append((int(start), int(l)))


seed_soil = []
soil_fert = []
fert_water = []
water_light = []
light_temp = []
temp_hum = []
hum_loc = []

for line in c[1:]:
    if line == "":
        continue
    if line == "seed-to-soil map:":
        lookup = seed_soil
    elif line == "soil-to-fertilizer map:":
        lookup = soil_fert
    elif line == "fertilizer-to-water map:":
        lookup = fert_water
    elif line == "water-to-light map:":
        lookup = water_light
    elif line == "light-to-temperature map:":
        lookup = light_temp
    elif line == "temperature-to-humidity map:":
        lookup = temp_hum
    elif line == "humidity-to-location map:":
        lookup = hum_loc
    else:
        (source_start, dest_start, length) = [int(i) for i in re.findall(r"\d+", line)]
        lookup.append((source_start, dest_start, length))


def find_in_lookup(lookup, source):
    for (source_start, dest_start, length) in lookup:
        if source > source_start and source_start+length >= source:
            return dest_start + (source - source_start)
    else:
        return source


def seed_exists(seed):
    for (start, length) in seed_pairs:
        if seed > start and seed < (start+length):
            return True


loc = 0
while True:
    hum = find_in_lookup(hum_loc, loc)
    temp = find_in_lookup(temp_hum, hum)
    light = find_in_lookup(light_temp, temp)
    water = find_in_lookup(water_light, light)
    fert = find_in_lookup(fert_water, water)
    soil = find_in_lookup(soil_fert, fert)
    seed = find_in_lookup(seed_soil, soil)
    if seed_exists(seed):
        print(loc -1)
        break
    loc += 1

