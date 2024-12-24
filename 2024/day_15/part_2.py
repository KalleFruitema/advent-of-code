from copy import deepcopy


with open("2024/day_15/input.txt") as file:
    grid, moves = file.read().strip().split("\n\n")
    grid = [list(line.strip()) for line in grid.split("\n")]
    moves = moves.strip().replace("\n", "")

expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}
grid = [list("".join(expansion[char] for char in line)) for line in grid]

move_dict = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0)
}

for y, row in enumerate(grid):
    for x, val in enumerate(row):
        if val == "@":
            start = (x, y)

x, y = start
for move in moves:
    dx, dy = move_dict[move]
    targets = [(x, y)]
    good = True
    for tx, ty in targets:
        nx, ny = tx + dx, ty + dy
        if (nx, ny) in targets:
            continue
        char = grid[ny][nx]
        if char == "#":
            good = False
            break
        elif char == "[":
            targets.append((nx, ny))
            targets.append((nx + 1, ny))
        elif char == "]":
            targets.append((nx, ny))
            targets.append((nx - 1, ny))
    if not good:
        continue
    grid2 = [list(row) for row in grid]
    grid[y][x] = "."
    grid[y + dy][x + dx] = "@"
    for bx, by in targets[1:]:
        grid[by][bx] = "."
    for bx, by in targets[1:]:
        grid[by + dy][bx + dx] = grid2[by][bx]
    x += dx
    y += dy

print(sum(y * 100 + x for y, row in enumerate(grid) for x, val in enumerate(row) if val == "["))