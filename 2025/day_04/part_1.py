with open("input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

adjacent = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)

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
                accessible += 1

print(accessible)
