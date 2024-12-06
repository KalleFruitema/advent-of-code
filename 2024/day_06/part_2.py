with open("2024/day_06/input.txt") as file:
    data = [list(line.strip()) for line in file if line.strip() != ""]


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()


breaker = False
for y, row, in enumerate(data):
    for x, val in enumerate(row):
        if val == "^":
            breaker = True
            guard = x, y
            break  
    if breaker:
        break

data[y][x] = "."

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
covered = {(x, y, directions[0])}

def walk_path(x, y, direction, part2=False):
    while True:
        ay, ax = direction
        nx, ny = x + ax, y + ay
        if 0 > nx or nx > len(data[0]) - 1 or 0 > ny or ny > len(data) - 1:
            break
        
        if data[ny][nx] == ".":
            x, y = nx, ny
        else:
            while data[ny][nx] != ".":
                direction = directions[(directions.index(direction) + 1) % len(directions)]
                ay, ax = direction
                nx, ny = x + ax, y + ay
            x, y = nx, ny
            if part2 and (x, y, direction) in covered:
                return True
        covered.add((x, y, direction))
    return False
        
walk_path(guard[0], guard[1], directions[0])

total = 0

for px, py in set(i[:2] for i in covered.copy()):
    covered.clear()
    data[py][px] = "%"
    infinite= walk_path(guard[0], guard[1], directions[0], part2=True)
    data[py][px] = "."
    total += infinite
    
print(total)