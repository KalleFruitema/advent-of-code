from heapq import heappop, heappush


with open("2024/day_16/input.txt") as file:
    grid = [line.strip() for line in file if line.strip() != ""]


for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "S":
            sx, sy = x, y
        elif val == "E":
            ex, ey = x, y
            
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


def min_score():
    pq = []
    heappush(pq, (0, sx, sy, 1))
    seen = set()

    while pq:
        score, x, y, direction = heappop(pq)
        if (x, y) == (ex, ey):
            return score
        
        if (x, y, direction) in seen:
            continue
        
        seen.add((x, y, direction))
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                new_score = score + 1 + (1000 if direction != i else 0)
                heappush(pq, (new_score, nx, ny, i))
                
    return -1


print(min_score())