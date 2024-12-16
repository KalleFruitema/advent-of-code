from collections import defaultdict


with open("2024/day_12/test3_input.txt") as file:
    grid = [line.strip() for line in file if line.strip() != ""]


seen = set()
edge_tiles = defaultdict(lambda: [])
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


class SidePart:
    def __init__(self, dx, dy, x, y):
        self.dx = dx
        self.dy = dy
        self.x = x + 1
        self.y = y + 1
        
    def same_direction(self, dx, dy):
        return self.dx == dx and self.dy == dy
    
    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy and self.x == other.x and self.y == other.y
    
    
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.edges = []
    
    def add_edge(self, edge: SidePart):
        self.edges.append(edge)
        
    def remove_edge(self, dx, dy):
        for i, edge in enumerate(self.edges):
            if edge.same_direction(dx, dy):
                self.edges.pop(i)
                break
        
    def pop_edge(self):
        self.edges.pop()
        
    def __repr__(self) -> str:
        return str(len(self.edges))
    
    def __int__(self) -> int:
        return len(self.edges)
        


def expand_region(x, y, area = 0, sides = 0):
    if (x, y) in seen:
        return area, sides
    seen.add((x, y))
    tile = grid[y][x]
    area += 1
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] == tile:
                if (nx, ny) not in seen:
                    area, sides = expand_region(nx, ny, area, sides)
            else:
                
                edge_tiles[(x, y)].append(SidePart(dx, dy, nx, ny))
        else:
            edge_tiles[(x, y)].append(SidePart(dx, dy, nx, ny))
    return area, sides


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(f"{i}" for i in line))
    print()
    
    
edge_tiles_history = []

for y, row in enumerate(grid):
    for x, tile in enumerate(row):
        if (x, y) not in seen:
            area, sides = expand_region(x, y)
            edge_tiles_history.append((area, dict(edge_tiles)))
            edge_tiles.clear()
            
total = 0
directions2 = ((1, 0), (0, 1)) # O Z 

for area, edge_tiles in edge_tiles_history:
    grid2 = [[Tile(x, y) for x in range(len(grid[0]) + 2)] for y in range(len(grid) + 2)]
    for i, ((x, y), sideparts) in enumerate(edge_tiles.items()):
        for sidepart in sideparts:
            grid2[sidepart.y][sidepart.x].add_edge(sidepart)

    sides = 0
    seen_locs = set()
    seen_start_dir = set()
    print("#" * 50)
    gprint(grid2)
    while (locs := [(x, y) for y, row in enumerate(grid2) for x, _ in enumerate(row) if int(grid2[y][x]) > 0]):
        li = 0
        while li < len(locs):
            x, y = locs[li]
            if int(grid2[y][x]) <= 0:
                li += 1
                continue
            gprint(grid2)
            
            for i, (dx, dy) in enumerate(directions2):
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(grid2[0]) and 0 <= ny < len(grid2)) or ((x, y), (dx, dy)) in seen_start_dir:
                    continue
                if int(grid2[ny][nx]) > 0:
                    seen_start_dir.add(((x, y), (dx, dy)))
                    break
            else:
                print("shit")
                sides += 1
                grid2[y][x].pop_edge()
                continue
            seen_locs.add((x, y))
            grid2[y][x].remove_edge(dx, dy)
            while int(grid2[ny][nx]) > 0:
                seen_locs.add((nx, ny))
                grid2[ny][nx].remove_edge(dx, dy)
                nx, ny = nx + dx, ny + dy
                if not (0 <= nx < len(grid2[0]) and 0 <= ny < len(grid2)):
                    break

            sides += 1
            li = 0
    total += area * sides

print(total)