import numpy as np
from functools import lru_cache


with open("input.txt") as file:
    grid = np.array([[*line.strip()] for line in file if line.strip() != ""])


@lru_cache
def beam(y, x):
    ends = 0
    for i, char in enumerate(grid[:, x][y:]):
        if char == "^":
            ends += beam(y + i, x - 1)
            ends += beam(y + i, x + 1)
            
            break
        if y + i == len(grid) - 1:
            return ends + 1
    return ends


start = [(0, i) for i, y in enumerate(grid[0]) if y == "S"][0]

print(beam(*start))

