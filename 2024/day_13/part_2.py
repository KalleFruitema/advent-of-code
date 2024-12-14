from math import gcd
import re


with open("2024/day_13/input.txt") as file:
    data = file.read().strip().split("\n\n")
    
for i, part in enumerate(data):
    data[i] = tuple(zip(*re.findall(r"X(?:\+|=)(\d+), Y(?:\+|=)(\d+)", part.strip())))

total = 0

for i, (data_x, data_y) in enumerate(data):
    ax, bx, px = map(int, data_x)
    ay, by, py = map(int, data_y)
    px += 10000000000000
    py += 10000000000000
    if px % gcd(ax, bx) == 0 and py % gcd(ay, by) == 0:
        a = round((py - ((by * px) / bx)) / (ay - ((by * ax) / bx)))
        b = round((px - ax * a) / bx)
        if a * ax + b * bx == px and a * ay + b * by == py:
            total += 3 * a + b
        
        
print(total)