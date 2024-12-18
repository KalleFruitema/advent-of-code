from heapq import heappop, heappush
import re


with open("2024/day_18/input.txt") as file:
    data = [map(int, re.findall(r"\d+", line)) for line in file if line.strip() != ""]

rows = 71
cols = 71
ex, ey = 70, 70
corrupted = {(x, y): "." for y in range(cols) for x in range(rows)}
directions = ((0, -1), (1, 0), (0, 1), (-1, 0)) # N O Z W


def find_path():
    seen = set()
    pq = [(0, 0, 0)]
    while pq:
        steps, x, y = heappop(pq)
        if (x, y) in seen:
            continue
        seen.add((x, y))
        if (x, y) == (ex, ey):
            return steps
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if corrupted.get((nx, ny)) == ".":
                heappush(pq, (steps + 1, nx, ny))
    return -1
            

for i, (x, y) in enumerate(data):
    corrupted[(x, y)] = "#"
    if find_path() == -1:
        print(x, y, sep=",")
        break

    
