with open("2024/day_06/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]


breaker = False
for y, row, in enumerate(data):
    for x, val in enumerate(row):
        if val == "^":
            breaker = True
            break  
    if breaker:
        break

data[y] = data[y].replace("^", ".")

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
direction = directions[0]
covered = {(x, y)}
nx, ny = x, y

while True:
    ay, ax = direction
    nx, ny = x + ax, y + ay
    if 0 > nx or nx > len(data[0]) - 1 or 0 > ny or ny > len(data) - 1:
        break
    
    if data[ny][nx] == ".":
        x, y = nx, ny
    elif data[ny][nx] == "#":
        while data[ny][nx] == "#":
            direction = directions[(directions.index(direction) + 1) % len(directions)]
            ay, ax = direction
            nx, ny = x + ax, y + ay
        x, y = nx, ny
    covered.add((x, y))
    
print(len(covered))