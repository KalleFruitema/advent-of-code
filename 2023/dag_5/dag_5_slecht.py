from pprint import pprint
from tabnanny import check
import numpy as np


with open(r'2023/dag_5/input.txt') as file:
    content = [line.strip() for line in file]

seeds, content = content[0].split(":")[1].strip().split(" "), content[1:]

seeds = np.array([int(seed) for seed in seeds])

print("Parsing starting...")

n_content = []
for line in content:
    if line == '':
        n_content.append([])
    else:
        n_content[-1].append(line)

for i, line in enumerate(n_content):
    n_content[i] = [[int(element) for element in x.split(" ")] 
                  for y, x in enumerate(line) if y != 0]

print("Mapping starting...")

pprint(n_content)
maps = []
for ranges in n_content:
    map_list = []
    for dest_start, src_start, length in ranges:
        mapped = np.transpose((np.arange(src_start, src_start + length),
                              np.arange(dest_start, dest_start + length)))
        map_list.append(mapped)
    maps.append(map_list)


def check_map_val(map_list, val):
    for y in map_list:
        if val in y[:, 0]:
            return y[np.where(val == y[:, 0])[0], 1][0]
    return val

    

print("Using maps...")

seed_dict = {}
for seed in seeds:
    # print(maps[0])
    # break
    soil = check_map_val(maps[0], seed)
    fertilizer = check_map_val(maps[1], soil)
    water = check_map_val(maps[2], fertilizer)
    light = check_map_val(maps[3], water)
    temperature = check_map_val(maps[4], light)
    humidity = check_map_val(maps[5], temperature)
    location = check_map_val(maps[6], humidity)
    
    seed_dict[seed] = {
        "soil": soil,
        "fertilizer": fertilizer,
        "water": water,
        "light": light,
        "temperature": temperature,
        "humidity": humidity,
        "location": location
    }

print("Finding lowest...")

lowest = None
for seed, vals in seed_dict.items():
    loc = vals["location"]
    if type(lowest) != int:
        lowest = loc
    elif loc < lowest:
        lowest = loc
pprint(seed_dict, sort_dicts=False)
print(lowest)