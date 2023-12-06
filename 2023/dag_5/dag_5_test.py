from pprint import pprint
from random import seed
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


# def check_map_val(ranges, seed_start, seed_len):
#     print("Seeds: ", range(seed_start, seed_start + seed_len))
#     for dest_start, src_start, length in ranges:
#         print("Source: ", range(src_start, src_start + length))
#         print("Destination: ", range(dest_start, dest_start + length))
#         range_max = max(src_start, seed_start)
#         range_min = min(src_start + length, seed_start + seed_len)
#         print(list(range(range_max, range_min, -1).__reversed__()))
#         # print(list(enumerate(range(range_max, range_min, -1).__reversed__(), 
#         #                      start=dest_start)))
#         break
#     return

# test1 = range(5, 0).__reversed__()
# test2 = range(0, 5).__reversed__()
# print(test1, test2)
# print(list(enumerate(test1)))
# print(list(enumerate(test2)))

def check_seedrange(map_ranges, seed_start, seed_len):
    for dest_start, src_start, range_len in map_ranges:
        range1 = range(seed_start, seed_start + seed_len)
        range2 = range(src_start, src_start + range_len)
        match_range = range(dest_start, dest_start + range_len)
        print("Seeds:   ", range1)
        print("Matching:", range2)
        intersect = [*sorted((min(range1[-1], range2[-1]), 
                              max(range1[0], range2[0])))]
        
        print()

pprint(seeds)
pprint(n_content)
# pprint(seeds)
for seed in seeds:
    soil = check_seedrange(n_content[0], *seed)
    # fertilizer = check_map_val(n_content[1], *soil)
    # water = check_map_val(n_content[2], *fertilizer)
    # light = check_map_val(n_content[3], *water)
    # temperature = check_map_val(n_content[4], *light)
    # humidity = check_map_val(n_content[5], *temperature)
    # location = check_map_val(n_content[6], *humidity)
    
# pprint(n_content)
# pprint(seeds)
