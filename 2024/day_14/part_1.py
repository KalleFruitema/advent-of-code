from functools import reduce
from operator import mul
import re


with open("2024/day_14/input.txt") as file:
    data = [list(map(int, re.findall(r"(-?\d+)+", line.strip()))) for line in file if line.strip() != ""]

# width = 11
# height = 7
width = 101
height = 103
half_width = width // 2
half_height = height // 2
seconds = 100


class Guard:
    def __init__(self, x, y, vx, vy) -> None:
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        
    def move(self, seconds = 1):
        self.x = (self.x + self.vx * seconds) % width
        self.y = (self.y + self.vy * seconds) % height
        
    def find_quadrant(self) -> int:
        if self.x < half_width:
            if self.y < half_height:
                return 0
            elif self.y > half_height:
                return 2
            else:
                return -1
        elif self.x > half_width:
            if self.y < half_height:
                return 1
            elif self.y > half_height:
                return 3
            else:
                return -1
        else:
            return -1
            

guards = []
for x, y, vx, vy in data:
    guards.append(Guard(x, y, vx, vy))
    
for guard in guards:
    guard.move(seconds)
    

quadrants = [0, 0, 0, 0]
for guard in guards:
    quadrant = guard.find_quadrant()
    if quadrant != -1:
        quadrants[quadrant] += 1

print(reduce(mul, quadrants))