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
        
get_to_z = []
which_z = []
for curr_loc in starting_locs:
    counter = 0
    steps = 0
    while True:
        if counter >= len(instructions):
            counter = 0
        instr = instructions[counter]
        counter += 1
        curr_loc = map_dict[curr_loc][instr]
        steps += 1
        if curr_loc[2] == "Z":
            break
    get_to_z.append(steps)
    which_z.append(curr_loc)

# tweede loop voor demonstratie
to_z_again = [] 
which_z2 = []
for curr_loc in which_z:
    counter = 0
    steps = 0
    while True:
        if counter >= len(instructions):
            counter = 0
        instr = instructions[counter]
        counter += 1
        curr_loc = map_dict[curr_loc][instr]
        steps += 1
        if curr_loc[2] == "Z":
            break
    to_z_again.append(steps)
    which_z2.append(curr_loc)

    
pprint(list(zip(starting_locs, get_to_z, which_z, to_z_again, which_z2)))
print(lcm(*get_to_z))