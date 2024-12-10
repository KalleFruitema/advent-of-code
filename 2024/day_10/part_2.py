with open("2024/day_10/input.txt") as file:
    grid = [tuple(int(a) if a != "." else a for a in line.strip()) for line in file if line.strip() != ""]

directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W
    
starts = []

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == 0:
            starts.append((x, y))
            
count = 0

def follow_path(x, y):
    current = grid[y][x]
    next = current + 1
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] == next:
            
            if next == 9:
                global count
                count += 1
            else:
                follow_path(nx, ny)
              
total = 0

for sx, sy in starts:
    follow_path(sx, sy)
    total += count

    count = 0
    
print(total)

