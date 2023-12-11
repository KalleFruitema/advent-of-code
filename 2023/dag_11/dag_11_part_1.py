from pprint import pprint
from copy import deepcopy


def print_grid(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(line))
    print()


with open("2023/dag_11/input.txt") as file:
    grid = [list(line.strip()) for line in file]
   
   
count = 0
for i, line in enumerate(grid.copy()):
    if "#" in line:
        continue
    grid.insert(i + count, line)
    count += 1


count = 0
grid_copy = deepcopy(grid)
row_len = len(grid[0].copy())
for i in range(row_len):
    row = [line[i] for line in grid_copy]
    if "#" in row:
        continue
    for line in grid:
        line.insert(i + count, ".")
    count += 1

for i, line in enumerate(grid):
    grid[i] = line[:row_len + count]
    

count = 1
all_solar = []
for y, line in enumerate(grid):
    for x, element in enumerate(line):
        if element == "#":
            grid[y][x] = str(count)
            all_solar.append((str(count), (y, x)))
            count += 1

pairs = []
for i, solar in enumerate(all_solar):
    for other_solar in all_solar[i + 1:]:
        pairs.append((solar, other_solar))


total_dist = 0
for solar1, solar2 in pairs:
    val1 = sorted([solar1[1][1], solar2[1][1]], reverse=True)
    val2 = sorted([solar1[1][0], solar2[1][0]], reverse=True)
    distance = (val1[0] - val1[1]) + (val2[0] - val2[1])
    total_dist += distance


print(total_dist)