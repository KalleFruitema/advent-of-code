from pprint import pprint
from shapely import Polygon, box, MultiPolygon


with open("2024/day_12/test1_input.txt") as file:
    grid = [line.strip() for line in file if line.strip() != ""]


seen = set()
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


def expand_region(x, y, coords) -> list[Polygon]:
    if (x, y) in seen:
        return coords
    seen.add((x, y))
    coords.append(box(x, y, x + 1, y + 1))
    tile = grid[y][x]
    possible = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == tile:
                if (nx, ny) not in seen:
                    possible.append((nx, ny))
    for nx, ny in possible:
        coords = expand_region(nx, ny, coords)
    return coords

shapes: list[Polygon] = []
for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) not in seen:
            boxes = expand_region(x, y, [])
            shape = MultiPolygon()
            for b in boxes:
                shape = shape.union(b)
            shapes.append(shape)


for shape in shapes:
    for poly in shape.geoms if hasattr(shape, "geoms") else [shape]:
        poly = poly.simplify(tolerance=1e-1)
        sides = len(poly.exterior.coords) - 1
        for interior in poly.interiors:
            sides += len(interior.coords) - 1
        print(sides)