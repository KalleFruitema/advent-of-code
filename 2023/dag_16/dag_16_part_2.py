with open("2023/dag_16/input.txt") as file:
    grid = [line.strip() for line in file]
   
   
def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
     
     
def transpose(grid):
    return tuple(zip(*grid))


def new_pos(y, x, direction):
    global visited
    try:
        match direction:
            case '>':
                for ax, val in enumerate(grid[y][x + 1:], start=1):
                    visited.add((y, x + ax))
                    if val not in '.-':
                        break
                (ny, nx) = (y, x + ax)
            case '<':
                for ax, val in enumerate(grid[y][:x][::-1], start=1):
                    visited.add((y, x - ax))
                    if val not in '.-':
                        break
                (ny, nx) = (y, x - ax)
            case '^':
                for ay, val in enumerate(transpose(grid)[x][:y][::-1], start=1):
                    visited.add((y - ay, x))
                    if val not in '.|':
                        break
                (ny, nx) = (y - ay, x)
            case 'v':
                for ay, val in enumerate(transpose(grid)[x][y + 1:], start=1):
                    visited.add((y + ay, x))
                    if val not in '.|':
                        break
                (ny, nx) = (y + ay, x)
            case _:
                raise UnboundLocalError
    except UnboundLocalError:
        (ny, nx) = -1, -1
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


def charge_grid():
    n_grid = [list('.' * len(line)) for line in grid]
    for y, x in visited:
        n_grid[y][x] = '#'
    return n_grid


def walk(startpos: tuple[int, int], startdir: str):
    global visited
    global used_splits

    ny, nx = new_pos(*startpos, startdir)
        
    if ny >= len(grid) or ny < 0 or\
        0 >= nx >= len(grid[0]) or nx < 0:
        return
    
    new_dir = new_direction(ny, nx, startdir)
    if new_dir in "-|":
        if (ny, nx) in used_splits:
            return
        else:
            used_splits.add((ny, nx))
            
    visited.add((ny, nx))
    if new_dir == "|":
        walk((ny, nx), '^')
        walk((ny, nx), 'v')
        return
    elif new_dir == "-":
        walk((ny, nx), '<')
        walk((ny, nx), '>')
        return
    walk((ny, nx), new_dir)


def get_starts():
    starts = []

    for x in range(len(grid[0])):
        startp = (0, x)
        startd = new_direction(*startp, 'v')
        starts.append((startp, startd))

    for x in range(len(grid[-1])):
        startp = (len(grid) - 1, x)
        startd = new_direction(*startp, '^')
        starts.append((startp, startd))

    for y in range(len(grid)):
        startp = (y, 0)
        startd = new_direction(*startp, '>')
        starts.append((startp, startd))
        
    for y in range(len(grid)):
        startp = (y, len(grid[0]) - 1)
        startd = new_direction(*startp, '<')
        starts.append((startp, startd))
    return starts
    
    
starts = get_starts()

all_totals = []
for startpos, startdir in starts:
    visited = set()
    used_splits = set()
    visited.add(startpos)
    walk(startpos, startdir)
    total = sum(line.count("#") for line in charge_grid())
    all_totals.append(total)

print(max(all_totals))