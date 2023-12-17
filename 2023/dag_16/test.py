def transpose(grid):
    return [line for line in zip(*grid)]


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
with open("2023/dag_16/input_test1.txt") as file:
    grid = [line.strip() for line in file]

gprint(grid)
gprint(transpose(grid))