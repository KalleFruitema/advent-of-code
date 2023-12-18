def input():
    with open("2023/dag_17/input_test1.txt", 'r') as file:
        content = [line.strip() for line in file]
        
    return content


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def transpose(grid):
    return list(zip(*grid))


grid = input()
gprint(grid)