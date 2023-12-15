from typing import Any
import numpy as np


def gprint(grid: list[list[Any]]):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()


def transpose(grid: list[list[Any]]) -> list[list[Any]]:
    return [list(line) for line in zip(*grid)]


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


with open("2023/dag_14/input_test1.txt", 'r') as file:
    grid = [list(line.strip()) for line in file]
    
    
cache_dict = {}


def gravity(grid):
    new_grid = []
    for line in grid:
        global cache_dict
        n_line = []
        for part in ("".join(line).split("#")):
            if tuple(part) in cache_dict:
                n_line.append(cache_dict[tuple(part)])
            else:
                sort_part = "".join(sorted(part))
                cache_dict.update({
                    part: sort_part
                })
                n_line.append(sort_part)
        new_grid.append(list("#".join(n_line)))
    return new_grid


gprint(grid)
grid = np.rot90(np.rot90(np.rot90(grid)))
for _ in range(1_000_000_000):
    for _ in range(4):
        grid = gravity(grid)
        grid = np.rot90(np.rot90(np.rot90(grid)))
grid = np.rot90(grid)
gprint(grid)


total = 0
for i, line in enumerate(grid[::-1], start=1):
    total += list(line).count("O") * i
    
print(total)