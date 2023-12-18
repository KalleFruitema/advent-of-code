def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def transpose(grid):
    return tuple(zip(*grid))


def input():
    with open("2023/dag_18/input.txt") as file:
        instructs = [line.strip().split(" ") for line in file]
    return instructs


def expand_grid(grid):
    grid.insert(0, ["~" for _ in range(len(grid[0]))])
    grid.append(["~" for _ in range(len(grid[0]))])
    for line in grid:
        line.insert(0, "~")
        line.append("~")
    return grid
    

def flood(grid: list[list[str]]):
    while True:
        water_pos = [(y, x) for y, line in enumerate(grid) for x, val in enumerate(line) if val == "~"]
        to_fill = set()
        for y, x in water_pos:
            to_fill.update([(sy, sx) for sy in range(y - 1, y + 2) for sx in range(x - 1, x + 2)
                            if 0 <= sy < len(grid) and 0 <= sx < len(grid[0]) and grid[sy][sx] == "."
                            and (sy, sx) not in water_pos])
            grid[y][x] = "$"
        if to_fill:
            for y, x in to_fill:
                grid[y][x] = "~"
        else:
            break
    return grid
            

def fill(grid):
    for line in grid:
        for i, val in enumerate(line):
            if val == ".":
                line[i] = "#"
    return grid


def drill(instructs):
    grid = [["#"]]
    y, x = 0, 0
    for direc, dist, color in instructs:
        for _ in range(int(dist)):
            if direc == "R":
                x += 1
                try:
                    if 0 > x:
                        raise IndexError
                    grid[y][x] = '#'
                except IndexError:
                    for line in grid:
                        line.append(".")
                    grid[y][x] = '#'
            elif direc == "L":
                x -= 1
                try:
                    if 0 > x:
                        raise IndexError
                    grid[y][x] = '#'
                except IndexError:
                    x += 1
                    for line in grid:
                        line.insert(0, '.')
                    grid[y][x] = '#'
            elif direc == "U":
                y -= 1
                try:
                    if 0 > y:
                        raise IndexError
                    grid[y][x] = '#'
                except IndexError:
                    y += 1
                    grid.insert(0, ['.' for _ in range(len(grid[0]))])
                    grid[y][x] = '#'
            elif direc == "D":
                y += 1
                try:
                    if 0 > y:
                        raise IndexError
                    grid[y][x] = '#'
                except IndexError:
                    grid.append(['.' for _ in range(len(grid[0]))])
                    grid[y][x] = '#'
    return grid
        
        
def count_area(grid):
    total = 0
    for line in grid:
        total += line.count("#")
    return total
         
         
def save_grid(grid):
    with open("2023/dag_18/grid.txt", "w") as gridfile:
       gridfile.write("\n".join("".join(line) for line in grid))
       

def main():
    instructs = input()
    grid = drill(instructs)
    grid = expand_grid(grid)
    # gprint(grid)
    # save_grid(grid)
    grid = flood(grid)
    # save_grid(grid)
    # gprint(grid)
    grid = fill(grid)
    # save_grid(grid)
    # gprint(grid)
    
    print(count_area(grid))
    
    
if __name__ == "__main__":
    main()
