from collections import deque
from functools import cache
from itertools import product
from pprint import pprint
import re


with open("2024/day_21/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

dirpad = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]

numdict = {}

for y, row in enumerate(numpad):
    for x, val in enumerate(row):
        numdict[val] = (x, y)
        
dirdict = {}

for y, row in enumerate(dirpad):
    for x, val in enumerate(row):
        dirdict[val] = (x, y) 


directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)} # N O Z W

def custom_sort(char):
    return "<>v^".index(char)


@cache
def move(x, y, gx, gy, keypad):
    grid = numpad if keypad == "num" else dirpad
    queue = deque([(0, "", x, y)])
    seen = set()
    possible = []
    shortest = float("inf")
    while queue:
        steps, moves, x, y = queue.popleft()
        
        if steps > shortest:
            break
        
        if (x, y) == (gx, gy):
            possible.append(moves + "A")
            shortest = steps
            continue
            
        if (x, y, moves) in seen:
            continue
        
        seen.add((x, y, moves))
        
        for char, (dx, dy)  in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] != "#":
                queue.append((steps + 1, moves + char, nx, ny))
                
    return possible

total = 0    

for line in data:
    x, y = numdict["A"]
    robot1 = []
    for char in line:
        gx, gy = numdict[char]
        robot1.append(move(x, y, gx, gy, "num"))
        x, y = gx, gy
    robot1 = ["".join(i) for i in product(*robot1)]

    prev_robot = robot1
    for i in range(2):
        n_robot = []
        x, y = dirdict["A"]
        for possible in prev_robot:
            tmp = []
            for char in possible:
                gx, gy = dirdict[char]
                tmp.append(move(x, y, gx, gy, "dir"))
                x, y = gx, gy
            n_robot.append(tmp)
        
        n_robot = ["".join(i) for x in n_robot for i in product(*x)]
        minlen = min(map(len, n_robot))
        n_robot = [i for i in n_robot if len(i) == minlen]
        prev_robot = n_robot
    
    total += len(min(n_robot, key=len)) * int(re.findall(r"\d+", line)[0])

print(total)