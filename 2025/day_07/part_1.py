import numpy as np


with open("input.txt") as file:
    grid = np.array([[*line.strip()] for line in file if line.strip() != ""])


count = 0
seen = set()

def beam(y, x):
    global count, seen
    
    for i, char in enumerate(grid[:, x][y:]):
        if char == "^":
            if (y + i, x) in seen:
                break
            seen.add((y + i, x))
            count += 1
            beam(y + i, x - 1)
            beam(y + i, x + 1)
            
            break


start = [(0, i) for i, y in enumerate(grid[0]) if y == "S"][0]

beam(*start)

print(count)