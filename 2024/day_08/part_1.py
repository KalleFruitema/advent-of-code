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
    for i, (x, y) in enumerate(locs):
        for x2, y2 in locs[i + 1:]:
            nx1, ny1 = (x + (x - x2), y + (y - y2))
            nx2, ny2 = (x2 + (x2 - x), y2 + (y2 - y))
            if 0 <= nx1 < len(data[0]) and 0 <= ny1 < len(data):
                antinodes.add((nx1, ny1))
            if 0 <= nx2 < len(data[0]) and 0 <= ny2 < len(data):
                antinodes.add((nx2, ny2))

print(len(antinodes))