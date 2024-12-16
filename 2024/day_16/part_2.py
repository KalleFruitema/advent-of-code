from collections import deque
from heapq import heappop, heappush


with open("2024/day_16/input.txt") as file:
    grid = [list(line.strip()) for line in file if line.strip() != ""]


for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "S":
            sx, sy = x, y
        elif val == "E":
            ex, ey = x, y
            
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W
seen = {}


def find_min_score():
    pq = []
    heappush(pq, (0, sx, sy, 1, 1))
    global seen
    
    while pq:
        score, x, y, direction, tiles = heappop(pq)
        
        if (x, y) == (ex, ey):
            return score
        
        if (x, y, direction) in seen and seen[(x, y, direction)] <= score:
            continue
        
        seen[(x, y, direction)] = score
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                new_score = score + 1 + (1000 if direction != i else 0)
                heappush(pq, (new_score, nx, ny, i, tiles + 1))
                
    return -1


min_score = find_min_score()
print(min_score)


def backtrack(min_turns):
    queue = deque([(ex, ey, min_turns)])
    best_tiles = set()
    best_tiles.add((ex, ey))

    while queue:
        x, y, remaining_score = queue.popleft()

        for i, (dx, dy) in enumerate(directions):
            nx, ny = x - dx, y - dy  # Reverse direction

            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                for d in range(4):
                    new_remaining_score = remaining_score - (1000 if d != i else 0) - 1
                    if (nx, ny, d) in seen and seen[(nx, ny, d)] == new_remaining_score:
                        best_tiles.add((nx, ny))
                        queue.append((nx, ny, new_remaining_score))

    return len(best_tiles)

print(backtrack(min_score))
