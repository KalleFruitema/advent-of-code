def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def transpose(grid):
    return tuple(zip(*grid))
