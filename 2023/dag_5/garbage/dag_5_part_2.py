from pprint import pprint
import numpy as np


with open(r'2023/dag_5/input_test.txt') as file:
    content = [line.strip() for line in file]

seeds, content = content[0].split(":")[1].strip().split(" "), content[1:]

seeds = np.array([int(seed) for seed in seeds])
seeds_length = int(len(seeds)/2)
seeds = np.reshape(seeds, (seeds_length, 2))


n_content = []
for line in content:
    if line == '':
        n_content.append([])
    else:
        n_content[-1].append(line)

for i, line in enumerate(n_content):
    n_content[i] = [[int(element) for element in x.split(" ")] 
                  for y, x in enumerate(line) if y != 0]


def check_map_val(ranges, mapped_val):
    for dest_start, src_start, length in ranges:
        if src_start <= mapped_val < src_start + length:
            return (dest_start + (mapped_val - src_start))
    return mapped_val


seed_dicts = []

for seed_range, seed_len in seeds:
    for seed in range(seed_range, seed_range + seed_len):
        soil = check_map_val(n_content[0], seed)
        fertilizer = check_map_val(n_content[1], soil)
        water = check_map_val(n_content[2], fertilizer)
        light = check_map_val(n_content[3], water)
        temperature = check_map_val(n_content[4], light)
        humidity = check_map_val(n_content[5], temperature)
        location = check_map_val(n_content[6], humidity)
    
        seed_dicts.append({
            "soil": soil,
            "fertilizer": fertilizer,
            "water": water,
            "light": light,
            "temperature": temperature,
            "humidity": humidity,
            "location": location
        })

lowest = 9999999999999999999999999999999999999
for seed in seed_dicts:
    loc = seed["location"]
    if loc < lowest:
        lowest = loc
# pprint(seed_dicts, sort_dicts=False)

print(lowest)