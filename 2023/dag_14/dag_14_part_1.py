from typing import Any


def gprint(grid: list[list[Any]]):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()


def rev_transpose(grid: list[list[Any]]) -> list[list[Any]]:
    return [list(line) for line in zip(*grid[::-1])][::-1]


def find_last_dot(line: list[str], curr_i: int):
    new_i = curr_i
    for i, item in enumerate(line):
        if item == "#":
            break
        if item == ".":
            new_i = curr_i + i
    return new_i


with open("2023/dag_14/input.txt", 'r') as file:
    grid = [list(line.strip()) for line in file]
    
grid = rev_transpose(grid)

for ri, line in enumerate(grid):
    for i in range(len(line)):
        item = line[i]
        if item == "O":
            if "." not in line[i:]:
                break
            new_pos = find_last_dot(line[i:], i)
            grid[ri][i], grid[ri][new_pos] = grid[ri][new_pos], grid[ri][i]

grid = rev_transpose(grid)

total = 0
for i, line in enumerate(grid[::-1], start=1):
    total += line.count("O") * i
    
print(total)