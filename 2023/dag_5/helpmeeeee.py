from pprint import pprint
import numpy as np


class ExitLoop(Exception):
    pass


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


def len_ranges(*range: range):
    return sum(len(i) for i in range)


def check_seedrange(seedrange_lst, mapranges, prints=True):
    if type(seedrange_lst) != list:
        seedrange_lst = [seedrange_lst]
    unused = seedrange_lst.copy()
    used = []

    for seedrange in unused:
        for dest_range, src_range in mapranges:
            intersect = find_intersection(seedrange, src_range)
            if prints:
                print(intersect)
            
            if intersect:
                dest_intersect = range(dest_range[intersect[0] - src_range[0]], 
                                        dest_range[intersect[0] - src_range[0] + len(intersect)])
                used.append(dest_intersect)
                if intersect[0] == seedrange[0]:
                    if intersect[-1] == seedrange[-1]:
                        # seed fully contained
                        break
                    else:
                        # left contained
                        unused.append(range(intersect[-1] + 1, 
                                            seedrange[-1] + 1))
                elif intersect[-1] == seedrange[-1]:
                    # right fully contained
                    unused.append(range(seedrange[0],
                                        intersect[0]))
                else:
                    # source fully contained
                    unused.append(range(seedrange[0],
                                        intersect[0]))
                    unused.append(range(intersect[-1] + 1, 
                                        seedrange[-1] + 1))
    return used

seed_dicts = []
for seed in seeds:
    # print(seed)
    soil = check_seedrange(seed, n_content[0])
    print("VOOR FUNTIE", soil)
    fertilizer = check_seedrange(soil, n_content[1], prints=True)
    print(fertilizer)
    # water = check_seedrange(fertilizer, n_content[2])
    # light = check_seedrange(water, n_content[3])
    # temperature = check_seedrange(light, n_content[4])
    # humidity = check_seedrange(temperature, n_content[5])
    # location = check_seedrange(humidity, n_content[6])

    # seed_dicts.append({
    #     "soil": soil,
    #     "fertilizer": fertilizer,
    #     "water": water,
    #     "light": light,
    #     "temperature": temperature,
    #     "humidity": humidity,
    #     "location": location
    # })
    
# pprint(seed_dicts, sort_dicts=False)    