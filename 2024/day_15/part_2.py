with open("2024/day_15/test3_input.txt") as file:
    ogrid, moves = file.read().strip().split("\n\n")
    grid = []
    for line in ogrid.split("\n"):
        n_line = []
        for char in line.strip():
            if char == "O":
                n_line.extend("[]")
            elif char == "@":
                n_line.extend("@.")
            else:
                n_line.extend(char*2)
        grid.append(n_line)
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

gprint(grid)


def look_ahead(x, y, dx, dy, boxes: list[tuple[int, int]]):
    boxes.append((x, y))
    for ex in range(0, 2):
        nx1, ny1 = x + dx, y + dy
        nx2, ny2 = x + dx + ex, y + dy + ex
        if grid[ny1][nx1] == "#" or grid[ny2][nx2] == "#":
            return -1
        elif grid[ny1][nx1] == "[":
            return look_ahead(nx1, ny1, dx, dy, boxes)
        elif grid[ny2][nx2] == "[":
            return look_ahead(nx2, ny2, dx, dy, boxes)
        elif grid[ny1][nx1] == "]":
            return look_ahead(nx1 - 1, ny1 - 1, dx, dy, boxes)
        elif grid[ny2][nx2] == "]":
            return look_ahead(nx2 - 1, ny2 - 1, dx, dy, boxes)
        elif grid[ny1][nx1] == "." or grid[ny2][nx2] == ".":
            return boxes