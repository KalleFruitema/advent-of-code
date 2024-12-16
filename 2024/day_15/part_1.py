with open("2024/day_15/input.txt") as file:
    grid, moves = file.read().strip().split("\n\n")
    grid = [list(line.strip()) for line in grid.split("\n")]
    moves = moves.strip().replace("\n", "")

def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
      

move_dict = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "@":
            start_x, start_y = x, y


def move_robot(x, y, dx, dy):
    global grid
    nx, ny = x + dx, y + dy
    if grid[ny][nx] == "#":
        return x, y
    elif grid[ny][nx] == "O":
        while grid[ny][nx] == "O":
            nx, ny = nx + dx, ny + dy
        else:
            if grid[ny][nx] == "#":
                return x, y
            else:
                grid[ny][nx] = "O"
                grid[y + dy][x + dx] = "@"
                grid[y][x] = "."
                return x + dx, y + dy
    else:
        grid[ny][nx] = "@"
        grid[y][x] = "."
        return nx, ny


x, y = start_x, start_y
for move in moves:
    dx, dy = move_dict[move]
    x, y = move_robot(x, y, dx, dy)
    
    
total = 0
for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "O":
            total += 100* y + x
            
print(total)