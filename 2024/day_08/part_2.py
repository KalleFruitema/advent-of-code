from collections import defaultdict


with open("2024/day_08/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]


frequencies = defaultdict(lambda: [])
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char != ".":
            frequencies[char].append((x, y))
            
antinodes = set()
for freq, locs in frequencies.items():
    if len(locs) > 1:
        antinodes.update(locs)
    for i, (x, y) in enumerate(locs):
        for x2, y2 in locs[i + 1:]:
            dx, dy = (x - x2, y - y2)
            nx, ny = (x + dx, y + dy)
            while 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                antinodes.add((nx, ny))
                nx, ny = (nx + dx, ny + dy)
                
            dx, dy = (x2 - x, y2 - y)
            nx, ny = (x + dx, y + dy)
            while 0 <= nx < len(data[0]) and 0 <= ny < len(data):
                antinodes.add((nx, ny))
                nx, ny = (nx + dx, ny + dy)
            
print(len(antinodes))