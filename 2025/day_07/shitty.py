from collections import deque


with open("test_input.txt") as file:
    grid = [line.strip() for line in file if line.strip() != ""]

pq = deque()
for i, char in enumerate(grid[-2]):
    if grid[-2][i] == "^":
        pq.append((len(grid) - 2, i, 1))

adjacent = (
    (-2, -1), (-2, 1)
)

total = 0
seen = set()
for y, x, _ in pq:
    seen.add((y, x))

while pq:
    print(pq)
    y, x, splits = pq.popleft()
    
    for ay, ax in adjacent:
        ny = y + ay
        nx = x + ax
        if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])):
            continue
        if grid[ny][nx] == "^":
            if (ny, nx) not in seen:
                splits += 1
                seen.add((ny, nx))
            pq.append((ny, nx, splits))

    if grid[y-2][x] == "S":
        total += splits

print(total)