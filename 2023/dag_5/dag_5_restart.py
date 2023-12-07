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
    n_content[i] = [[int(element) for element in x.split(" ")] 
                     for y, x in enumerate(line) if y != 0]
content = n_content.copy()

pprint(seeds)
print()
pprint(content)

    
def map_seedrange(seedrange, map_ranges, prints=False):
    sects_list = []
    if type(seedrange) != list:
        seedrange = [seedrange]
    
    breaker = False
    map_idx = 0
    while True:
        if breaker:
            break
        
        for seed_part in seedrange:
            dest_start, src_start, length = map_ranges[map_idx]
            
            print(seed_part)

            src_range = range(src_start, src_start + length)
            dest_range = range(dest_start, dest_start + length)
            if prints:
                print(f"\n\nSeedrange:  {seed_part}\nSrc range:  {src_range}"
                    f"\nDest range: {dest_range}\n")
            min_val = min(src_start + length, seed_part[0] + len(seed_part))
            max_val = max(src_start, seed_part[0])

            intersection = range(max_val, min_val)
            if intersection:
                print(intersection)
                x = range(dest_range[intersection[0] - src_start], 
                        dest_range[intersection[0] - src_start + len(intersection)])
                
                if intersection[0] > seed_part[0]:
                    if intersection[-1] > seed_part[-1]:
                        print("right extend")
                        seedrange = [range(seed_part[0], intersection[0]), x]
                    else:
                        print("both extend")
                        seedrange = [range(seed_part[0], intersection[0]), x, range(intersection[-1], seed_part[-1])]
                else:
                    if intersection[-1] < seed_part[-1]:
                        print("left extend")
                        seedrange = x, [range(intersection[-1], seed_part[-1])]
                    else:
                        print("seed inside source")
                        breaker = True
                        seedrange = [x]
                break
            else:
                ...
            
    
    return seedrange
    
for seedrange in seeds:
    soil = map_seedrange(seedrange, content[0], prints=True)
    print(soil)
    fertilizer = []
    for soil_range in soil:
        fertilizer.extend(map_seedrange(soil_range, content[1], prints=True))
    print(fertilizer)
    break
    # fertilizer = map_seedrange(soil, n_content[1])
    # water = map_seedrange(fertilizer, n_content[2])
    # light = map_seedrange(water, n_content[3])
    # temperature = map_seedrange(light, n_content[4])
    # humidity = map_seedrange(temperature, n_content[5])
    # location = map_seedrange(humidity, n_content[6])
    # print(location)
    # break

