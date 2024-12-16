from collections import deque
from pprint import pprint


with open("2024/day_12/input.txt") as file:
    grid = [list(line.strip()) for line in file if line.strip() != ""]
    
seen = set()
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


def expand_region(x, y, region):
    if (x, y) in seen:
        return region
    seen.add((x, y))
    tile = grid[y][x]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == tile:
                if (nx, ny) not in seen:
                    region.add((nx, ny))
                    region = expand_region(nx, ny, region)
    return region


regions = []

for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) not in seen:
            regions.append(expand_region(x, y, {(x, y)}))


def sides(region):
    edges = {}
    for x, y in region:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in region:
                continue
            ex, ey = (x + nx) / 2, (y + ny) / 2
            edges[(ex, ey)] = (ex - x, ey - y)
    
    seen = set()
    side_count = 0
    for edge, direction in edges.items():
        if edge in seen:
            continue
        seen.add(edge)
        side_count += 1
        ex, ey = edge
        if ex % 1 == 0:
            for dx in [-1, 1]:
                cx = ex + dx
                while edges.get((cx, ey)) == direction:
                    seen.add((cx, ey))
                    cx += dx
        else:
            for dy in [-1, 1]:
                cy = ey + dy
                while edges.get((ex, cy)) == direction:
                    seen.add((ex, cy))
                    cy += dy
                    
    return side_count


total = sum(len(region) * sides(region) for region in regions)
print(total)