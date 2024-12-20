from heapq import heappop, heappush


with open("2024/day_20/input.txt") as file:
    grid = [list(line.strip()) for line in file if line.strip() != ""]


for y, line in enumerate(grid):
    for x, val in enumerate(line):
        if val == "S":
            start = x, y
        if val == "E":
            end = x, y


directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W
pq = [(0, *start)]
distances = [["#" if grid[y][x] == "#" else -1 for x in range(len(grid[0]))] for y in range(len(grid))]

while pq:
    pico, x, y = heappop(pq)
    
    if distances[y][x] != -1:
        continue
    
    distances[y][x] = pico
    
    if (x, y) == end:
        break
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
            heappush(pq, (pico + 1, nx, ny))


total = 0
for y, row in enumerate(distances):
    for x, val in enumerate(row):
        if val == "#":
            continue
        for r in range(2, 21):
            for dy in range(r + 1):
                dx = r - dy
                for nx, ny in {(x + dx, y + dy), (x + dx, y - dy), (x - dx, y + dy), (x - dx, y - dy)}:
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                        if distances[y][x] - distances[ny][nx] >= 100 + r:
                            total += 1
            
            
print(total)