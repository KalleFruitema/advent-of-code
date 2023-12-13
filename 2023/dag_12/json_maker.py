import json
from re import split


with open("2023/dag_12/input_test1.txt") as file:
    content = [line.strip().split(" ") for line in file]
    

grid, instructs = [], []
for line, inst in content:
    grid.append(line)
    instructs.append([int(i) for i in inst.split(",")])
    
all_possible = {}

for line, instruc in zip(grid, instructs):
    s_line = [i for i in split(r"[.]", line) if i != ""]
    print(tuple([s_line, instruc]))