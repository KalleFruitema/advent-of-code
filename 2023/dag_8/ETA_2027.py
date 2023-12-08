from pprint import pprint
from math import lcm


with open("2023/dag_8/input.txt") as file:
    instructions, *maps = [line.strip().replace(" ", "") for line in file if line != "\n"]
    
map_dict = {}
for i, y in enumerate(maps):
    key, val = y.split("=")
    val = val.strip("()").split(",")
    map_dict[key] = {
        "L": val[0],
        "R": val[1]
    }

starting_locs = []
for loc in map_dict.keys():
    if loc[2] == "A":
        starting_locs.append(loc)
        
counter = 0
steps = 0
curr_loc_lst = starting_locs.copy()
while True:
    n_loc_lst = []
    if counter >= len(instructions):
        counter = 0
    instr = instructions[counter]
    counter += 1
    for i in range(len(starting_locs)):
        n_loc_lst.append(map_dict[curr_loc_lst[i]][instr])
    steps += 1
    
    for curr_loc in n_loc_lst:
        if curr_loc[2] != "Z":
            break
    else:
        break
    curr_loc_lst = n_loc_lst.copy()
    
print(steps)