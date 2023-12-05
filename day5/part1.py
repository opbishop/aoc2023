import math
import os
import re
from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

seeds = [int(i) for i in re.findall(r"\d+", c[0])]

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
    for (dest_start, source_start, length) in lookup:
        if source > source_start and source_start+length >= source:
            return dest_start + (source - source_start)
    else:
        return source
find_in_lookup(hum_loc, 35)
min_loc = math.inf
for seed in seeds:
    soil = find_in_lookup(seed_soil, seed)
    fert = find_in_lookup(soil_fert, soil)
    water = find_in_lookup(fert_water, fert)
    light = find_in_lookup(water_light, water)
    temp = find_in_lookup(light_temp, light)
    hum = find_in_lookup(temp_hum, temp)
    loc = find_in_lookup(hum_loc, hum)
    min_loc = min(min_loc, loc)
print(min_loc)