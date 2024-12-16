import sys
from shapely import box, MultiPolygon
from collections import defaultdict

shapes = defaultdict(MultiPolygon)

inp = [s.rstrip('\n') for s in open("2024/day_12/test1_input.txt")]
for r, line in enumerate(inp):
    for c, color in enumerate(line):
        shapes[color] = shapes[color].union( box(r, c, r + 1, c + 1) )

res = 0
res2 = 0
for color, polys in shapes.items():
    for poly in polys.geoms if hasattr(polys, "geoms") else [polys]:
        poly = poly.simplify(tolerance=1e-1)
        sides = len(poly.exterior.coords) - 1
        for interior in poly.interiors:
            sides += len(interior.coords) - 1
        res += poly.area * poly.length
        res2 += poly.area * sides

print(int(res))
print(int(res2))