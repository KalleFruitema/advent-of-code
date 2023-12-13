from pprint import pprint


def print_grid(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(line))
    print()


with open("2023/dag_13/input.txt", 'r') as file:
    content = [line.strip() for line in file]

mirror_lst = []
mirror = []
for line in content:
    if line == "":
        mirror_lst.append(mirror)
        mirror = []
    else:
        mirror.append(list(line))
if mirror != []:
    mirror_lst.append(mirror)

    
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
                return i
    return 0


def transpose(mirror):
    return [line for line in zip(*mirror)]


totalvert = 0
totalhor = 0
for mirror in mirror_lst:
    totalhor += check_rows(mirror)
    totalvert += check_rows(transpose(mirror))
    
print(totalvert + (100 * totalhor))