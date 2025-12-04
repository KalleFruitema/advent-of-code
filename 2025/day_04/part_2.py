with open("input.txt") as file:
    data = [list(line.strip()) for line in file if line.strip() != ""]

adjacent = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)

total = 0

while True:
    locs = []
    accessible = 0

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '@':
                count = 0
                for ay, ax in adjacent:
                    ny = y + ay
                    nx = x + ax
                    if not (0 <= ny < len(data) and 0 <= nx < len(line)):
                        continue
                    elif data[ny][nx] == "@":
                        count += 1
                        
                    if count >= 4:
                        break
                else:
                    locs.append((y, x))
                    accessible += 1
    
    if accessible == 0:
        break
    
    for y, x in locs:
        data[y][x] = "."
    
    total += accessible

print(total)
