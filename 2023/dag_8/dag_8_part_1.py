from pprint import pprint


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

counter = 0
steps = 0
curr_loc = "AAA"
while True:
    if counter >= len(instructions):
        counter = 0
    instr = instructions[counter]
    counter += 1
    curr_loc = map_dict[curr_loc][instr]
    steps += 1
    if curr_loc == "ZZZ":
        break

print(steps)
    