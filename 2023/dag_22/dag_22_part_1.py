import numpy as np
from useful import *

with open("2023/dag_22/input.txt") as file:
    bricks = [[[int(x) for x in i.split(",")] 
               for i in line.strip().split("~")] 
              for line in file]
    
max_x = max(set(x[0] for i in bricks for x in i)) + 1
max_y = max(set(x[1] for i in bricks for x in i)) + 1
max_z = max(set(x[2] for i in bricks for x in i)) + 1

grid = np.zeros((max_x, max_y, max_z))

for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks, start=1):
    for nx in range(x1, x2 + 1):
        for ny in range(y1, y2 + 1):
            for nz in range(z1, z2 + 1):
                grid[nx][ny][nz] = i
                
print(grid)
print("\n")

