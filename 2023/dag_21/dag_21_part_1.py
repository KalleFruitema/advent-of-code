with open("2023/dag_21/input.txt") as file:
    grid = [list(line.strip()) for line in file]


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    

def find_startpos():
    for y, line in enumerate(grid):
        if "S" in line:
            return (y, line.index("S"))
    raise BrokenPipeError


def find_pos(sy, sx):
    global all_possible
    new_pos = []
    for i in range(-1, 2, 2):
        ny, nx = sy + i, sx + i
        if 0 <= ny < len(grid):
            new_pos.append((ny, sx))
        if 0 <= nx < len(grid[0]):
            new_pos.append((sy, nx))
    for pos in new_pos.copy():
        if grid[pos[0]][pos[1]] == "#":
            new_pos.remove(pos)
    return new_pos


def paint_grid(all_pos):
    global grid
    for y, x in all_pos:
        try:
            grid[y][x] = "O"
        except IndexError:
            pass


def main():
    all_pos = [find_startpos()]
    for _ in range(64):
        n_pos = set()
        for pos in all_pos:
            n_pos.update(find_pos(*pos))
        all_pos = n_pos
    # paint_grid(all_pos)
    # gprint(grid)
    print(len(all_pos))
    
        
if __name__ == "__main__":
    main()
    