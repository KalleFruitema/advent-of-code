import sys


all_possible = set()
sys.setrecursionlimit(64)


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
    for pos in new_pos:
        if grid[pos[0]][pos[1]] == "#":
            continue
        try:
            find_pos(pos[0], pos[1])
        except RecursionError:
            all_possible.add(pos)


def paint_grid():
    global grid
    for y, x in all_possible:
        try:
            grid[y][x] = "O"
        except IndexError:
            pass


def main():
    sy, sx = find_startpos()
    find_pos(sy, sx)
    # paint_grid()
    # gprint(grid)
    print(len(all_possible))
    
        
if __name__ == "__main__":
    main()
    