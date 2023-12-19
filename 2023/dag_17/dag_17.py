from heapq import heappush, heappop, nsmallest, merge
from random import randint


def input():
    with open("2023/dag_17/input_test1.txt", 'r') as file:
        content = [line.strip() for line in file]
        
    return content


def gprint(grid):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()
    
    
def find_path(grid):
    queue = []
    


def main():    
    grid = input()
    gprint(grid)
    path = find_path(grid)
    
    
if __name__ == "__main__":
    main()
    