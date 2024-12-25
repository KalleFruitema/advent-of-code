from collections import deque
from functools import cache
from itertools import product
import re


def compute_seqs(keypad):
    pos = {}
    for y, row in enumerate(keypad):
        for x, val in enumerate(row):
            if val == "#": continue
            pos[val] = (x, y)
    seqs = {}
    for a, a_loc in pos.items():
        for b, b_loc in pos.items():
            if a == b:
                seqs[(a, b)] = ["A"]
                continue
            
            possible = []
            queue = deque([(a_loc, "")])
            shortest = float("inf")
            
            while queue:
                (x, y), moves = queue.popleft()
                for move, (dx, dy) in directions.items():
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= len(keypad[0]) or ny >= len(keypad): continue
                    if keypad[ny][nx] == "#": continue
                    if keypad[ny][nx] == b:
                        if shortest < len(moves) + 1: 
                            break
                        shortest = len(moves) + 1
                        possible.append(moves + move + "A")
                    else:
                        queue.append(((nx, ny), moves + move))
                else:
                    continue
                break
            
            seqs[(a, b)] = possible
    return seqs


def solve(target, seqs):
    options = ["".join(i) for i in product(*[seqs[(a, b)] for a, b in zip("A" + target, target)])]
    return options
    
    
directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)} # N O Z W

numpad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

numseqs = compute_seqs(numpad)

dirpad = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]

dirseqs = compute_seqs(dirpad) 
dir_lengths = {k: len(v[0]) for k, v in dirseqs.items()}


@cache
def compute_length(a, b, depth=2):
    if depth == 1:
        return dir_lengths[(a, b)]
    shortest = float("inf")
    for seq in dirseqs[(a, b)]:
        length = 0
        for c, d in zip("A" + seq, seq):
            length += compute_length(c, d, depth - 1 )
        shortest = min(shortest, length)
    return shortest
        

with open("2024/day_21/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

total = 0

for line in data:
    robot1 = solve(line, numseqs)
    shortest = float("inf")
    for seq in robot1:
        length = 0
        for a, b in zip("A" + seq, seq):
            length += compute_length(a, b, depth=25)
        shortest = min(shortest, length)
        
    total += shortest * int(re.findall(r"\d+", line)[0])
    
print(total)