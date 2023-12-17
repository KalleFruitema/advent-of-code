import sys


# sys.setrecursionlimit(999999999)
visited = {(0, 0)}


with open("2023/dag_16/input_test1.txt") as file:
    grid = [line.strip() for line in file]
   
   
def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
     
     
gprint(grid)
startpos = (0, 0)
startdir = '>'


def new_pos(y, x, direction):
    match direction:
        case '>':
            (ny, nx) = (y, x + 1)
        case '<':
            (ny, nx) = (y, x - 1)
        case '^':
            (ny, nx) = (y - 1, x)
        case 'v':
            (ny, nx) = (y + 1, x)
        case _:
            raise UnboundLocalError(f"Waarom geef je me \'{direction}\'")
    return (ny, nx)


def new_direction(ny, nx, direction: str):
    match grid[ny][nx]:
        case '\\':
            transdict = {"^":"<", ">":"v"}
            for s, e in transdict.items():
                if s == direction:
                    return e
                elif e == direction:
                    return s
        case '/':
            transdict = {"^":">", "<":"v"}
            for s, e in transdict.items():
                if s == direction:
                    return e
                elif e == direction:
                    return s
        case '-':
            if direction in "><":
                return direction
            else:
                return '-'
        case '|':
            if direction in "^v":
                return direction
            else:
                return '|'
        case '.':
            return direction
    raise UnboundLocalError(f"Je geeft me \'({ny}, {nx})\' en \'{direction}\'")


count = 0


def walk(startpos: tuple[int, int], startdir: str):
    global count
    global visited
    print("recursion:", count)
    if count > 24:
        return
    count += 1
    
    print(visited)
    ny, nx = new_pos(*startpos, startdir)
    if ny >= len(grid) or ny < 0 or\
        0 >= nx >= len(grid[0]) or nx < 0:
        return
    # print(ny, nx)
    
    new_dir = new_direction(ny, nx, startdir)
    visited.add((ny, nx))
    print(ny, nx)
    if new_dir == "|":
        print("| split")
        walk((ny, nx), '^')
        walk((ny, nx), 'v')
        return
    elif new_dir == "-":
        print("- split")
        walk((ny, nx), '<')
        walk((ny, nx), '>')
        return
    print("default")
    walk((ny, nx), new_dir)

try:
    walk(startpos, startdir)
except RecursionError as e:
        print(e)
        # exit("Recursion error.")
        
# print(visited)

n_grid = [list('.' * len(line)) for line in grid]
for y, x in visited:
    n_grid[y][x] = '#'

gprint(n_grid)