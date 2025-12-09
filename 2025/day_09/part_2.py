from shapely import Polygon


with open("input.txt") as file:
    points = [tuple(map(int, line.strip().split(","))) for line in file if line.strip()]

allowed_area = Polygon(points)

largest = 0
for i, (x1, y1) in enumerate(points):
    for x2, y2 in points[i+1:]:
        rect = Polygon(((x1, y1), (x2, y1), (x2, y2), (x1, y2)))
        
        if allowed_area.contains(rect):
            surface = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            largest = max(largest, surface)

print(largest)