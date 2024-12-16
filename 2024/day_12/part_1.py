from operator import mul


with open("2024/day_12/input.txt") as file:
    grid = [line.strip() for line in file if line.strip() != ""]


seen = set()
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


def expand_region(x, y, area = 0, perimeter = 0):
    if (x, y) in seen:
        return area, perimeter
    seen.add((x, y))
    tile = grid[y][x]
    area += 1
    possible = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == tile:
                if (nx, ny) not in seen:
                    possible.append((nx, ny))
            else:
                perimeter += 1
        else:
            perimeter += 1
            
    for nx, ny in possible:
        area, perimeter = expand_region(nx, ny, area, perimeter)
    return area, perimeter


total = 0

for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) not in seen:
            total += mul(*expand_region(x, y))
            
print(total)