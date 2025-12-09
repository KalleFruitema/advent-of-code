with open("input.txt") as file:
    points = [tuple(map(int, line.strip().split(","))) for line in file if line.strip()]

largest = 0

for i, (x1, y1) in enumerate(points):
    for x2, y2 in points[i+1:]:
        surface = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        largest = max(largest, surface)

print(largest)
