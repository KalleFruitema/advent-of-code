from typing import Any


def gprint(grid: list[list[Any]]):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def transpose(grid: list[list[Any]]) -> list[list[Any]]:
    return list(zip(*grid))
