from pprint import pprint
import numpy as np


with open(r'2023/dag_5/input_test.txt') as file:
    content = [line.strip() for line in file]

seeds, content = content[0].split(":")[1].strip().split(" "), content[1:]

seeds = np.array([int(seed) for seed in seeds])
seeds_length = int(len(seeds)/2)
seeds = np.reshape(seeds, (seeds_length, 2))
seeds = [range(seed_start, seed_start + seed_len) 
         for seed_start, seed_len in seeds]

n_content = []
for line in content:
    if line == '':
        n_content.append([])
    else:
        n_content[-1].append(line)

for i, line in enumerate(n_content):
    ranges = [[int(element) for element in x.split(" ")] 
               for y, x in enumerate(line) if y != 0]
    n_content[i] = tuple((range(n_line[0], n_line[0] + n_line[2]), 
                          range(n_line[1], n_line[1] + n_line[2]))
                         for n_line in ranges)
content = n_content.copy()

# pprint(seeds)
# print()
# pprint(content)


def find_intersection(range1, range2):
    min_val = min(range1[-1], range2[-1])
    max_val = max(range1[0], range2[0])
    return range(max_val, min_val + 1)


def check_seedrange(seedranges, map_ranges):
    if type(seedranges) != list:
        seedranges = [seedranges]
    i = 0
    while True:
        for seed_part in seedranges:
            unused_list = []
            sect_list = []
            for dest_range, src_range in map_ranges:
                print(seed_part, src_range)
                intersection = find_intersection(seed_part, src_range)
                print(intersection)
                if intersection:
                    dest_intersection = range(dest_range[intersection[0] - src_range[0]], 
                        dest_range[intersection[0] - src_range[0] + len(intersection)])
                    if intersection[0] == seed_part[0]:
                        if intersection[-1] == seed_part[-1]:
                            # seed fully contained
                            ...
                        else:
                            # left contained
                            ...
                    elif intersection[-1] == seed_part[-1]:
                        # right fully contained
                        ...
                    else:
                        # source fully contained
                        ...

        break


check_seedrange(seeds[0], content[0])
            