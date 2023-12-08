from pprint import pprint
import numpy as np


class ExitLoop(Exception):
    pass


with open(r'2023/dag_5/input.txt') as file:
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


def find_intersection(range1, range2):
    min_val = min(range1[-1], range2[-1])
    max_val = max(range1[0], range2[0])
    return range(max_val, min_val + 1)


def len_ranges(*ranges: range):
    return sum(len(i) for i in ranges)


def min_ranges(*ranges: range):
    return min([i[0] for i in ranges])


def check_seedrange(seedrange_lst, mapranges):
    if type(seedrange_lst) != list:
        seedrange_lst = [seedrange_lst]
    unused = seedrange_lst.copy()
    used = []

    for seedrange in unused:
        # print(f"\nCURRENT SEED RANGE:\n{seedrange}\n")
        for dest_range, src_range in mapranges:
            # print("DEST", dest_range)
            # print("SRC", src_range)
            intersect = find_intersection(seedrange, src_range)
            # print(intersect)
            
            if intersect:
                # print(len(intersect))
                # print("START", intersect[0] - src_range[0])
                # print("END", intersect[0] - src_range[0] + len(intersect) - 1)
                dest_intersect = range(dest_range[src_range.index(intersect[0])],
                                       dest_range[src_range.index(intersect[-1])] + 1)
                # print("DEST_INTER", dest_intersect)
                # dest_intersect = range()
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
    # print("UNUSED:")
    for _range in unused:
        for i in range(unused.count(_range)):
            if i > 0:
                unused.remove(_range)
    # pprint(unused)
    
    used = sorted(list(set(used)), key=lambda x: x[0])
    unused = unused[::-1]
    fix_count = 0
    while len_ranges(*used) != len_ranges(*seedrange_lst):
        # waarom gaat dit fout yo wtf
        try:
            print(len_ranges(*used))
            print(len_ranges(*seedrange_lst))
            print()
            print(unused[fix_count])
            print()
            used.append(unused[fix_count])
        except Exception:
            print(len_ranges(*used))
            print(len_ranges(*seedrange_lst))
            print(unused)
            print()
            print(seedrange_lst)
            print()
            print(used)
            print(fix_count)
            exit()
        fix_count += 1
    return used

seed = range(50, 101)
maps = ((range(25,51), range(75,101)), 
        (range(0, 11), range(50, 61)))
# juist resultaat:
# range(25, 51), range(0, 11), range(61, 75)

seed_dicts = []
for seed in seeds:
    # print(seed)
    soil = check_seedrange(seed, n_content[0])
    # print("VOOR FUNTIE", soil)
    fertilizer = check_seedrange(soil, n_content[1])
    # print(fertilizer)
    water = check_seedrange(fertilizer, n_content[2])
    light = check_seedrange(water, n_content[3])
    temperature = check_seedrange(light, n_content[4])
    humidity = check_seedrange(temperature, n_content[5])
    location = check_seedrange(humidity, n_content[6])

    seed_dicts.append({
        "soil": soil,
        "fertilizer": fertilizer,
        "water": water,
        "light": light,
        "temperature": temperature,
        "humidity": humidity,
        "location": location
    })
    
lowest = 999999999999999999999999999999999999999
for seed_dict in seed_dicts:
    if (min_range := min_ranges(*seed_dict["location"])) < lowest:
        lowest = min_range
    
# pprint(seed_dicts, sort_dicts=False)

print(lowest)