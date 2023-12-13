grid = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]
grid2 = grid.copy()[::-1]
grid3 = [[1, 1, 1, 1], [2, 2, 1, 2], [3, 3, 3, 3], [4, 4, 4, 4], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]
grid4 = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 3], [4, 4, 4, 4], [3, 3, 3, 3], [2, 2, 2, 2]]


def transpose(mirror):
    return [line for line in zip(*mirror)]


def gprint(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join([str(i) for i in line]))
    print()


def check_rows(mirror):
    for i, row in enumerate(mirror):
        if i == 0:
            continue
        top, bot = mirror[i - 1], row
        if top == bot:
            i2 = 1
            correct = False
            while not correct:
                try:
                    if i - 1 - i2 < 0:
                        raise IndexError
                    top, bot = mirror[i - 1 - i2], mirror[i + i2]
                    i2 += 1
                    if top != bot:
                       break 
                except IndexError:
                    correct = True
            if correct:
                return (i - 1, i)
    return None
                

gprint(grid)
gprint(transpose(grid))
x = check_rows(grid)
print(x)

gprint(grid2)
y = check_rows(grid2)
print(y)

gprint(grid3)
z = check_rows(grid3)
print(z)

gprint(grid4)
w = check_rows(grid4)
print(w)
