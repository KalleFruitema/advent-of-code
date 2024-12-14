from collections import Counter
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
        
    def position(self) -> tuple[int, int]:
        return (x, y)
        
    def move(self, seconds = 1) -> None:
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

i = 0
while True:
    x_positions = []
    y_positions = []
    for guard in guards:
        guard.move()
        x_positions.append(guard.x)
        y_positions.append(guard.y)
    i += 1
    most_x = Counter(x_positions).most_common()[0][1]
    most_y = Counter(y_positions).most_common()[0][1]
    if most_x >= 30 and most_y >= 30:
        print(i)
        break
