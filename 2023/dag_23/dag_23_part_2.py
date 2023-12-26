with open("2023/dag_23/input_test1.txt") as file:
    grid = [list(line.strip()) for line in file]


paths = []
succesful_paths = []
 

def gprint(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def walk_path(path):
    global paths
    global succesful_paths
    while True:
        y, x = path[-1]
        
        surrounding = []
        for i in range(-1, 2, 2):
            ny, nx = y + i, x + i
            if 0 <= ny < len(grid):
                sq = grid[ny][x]
                if ((ny, x) not in path) and sq != "#":
                    surrounding.append((ny, x))
            if 0 <= nx < len(grid[0]):
                sq = grid[y][nx]
                if ((y, nx) not in path) and sq != "#":
                    surrounding.append((y, nx))
                    
        if len(surrounding) == 1:
            path.append(surrounding[0])
        else:
            for yy, xx in surrounding:
                paths.append([*path, (yy, xx)])
            break
    if path[-1] == (len(grid) - 1, grid[-1].index(".")):
        succesful_paths.append(path)
    

def paint_grid(path):
    for y, x in path:
        grid[y][x] = "O"


def main():
    global paths
    start = (0, grid[0].index("."))
    paths.append([start])
    for path in paths:
        walk_path(path)
    # paint_grid(paths[-1])
    # gprint(grid)
    print(sum(len(x) for x in succesful_paths))
    print(max(map(lambda x: len(x) - 1, succesful_paths)))
    

if __name__ == "__main__":
    main()
    