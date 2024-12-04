with open("2024/day_04/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]


starts = []

for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == "X":
            starts.append((y, x))
            
directions = ((-1,-1), (-1,0), (0,-1), (-1,1), (1,-1), (1,0), (0,1), (1,1))

def check_full(y, x, symbol, direction = None):
    if symbol == "S":
        return 1
    position = "XMAS".index(symbol)
    next_symbol = "XMAS"[position + 1]
    if direction is None:
        possible = []
        for direction in directions:
            ny, nx = y + direction[0], x + direction[1]
            if 0 <= nx < len(data) and 0 <= ny < len(data) and data[ny][nx] == next_symbol:
                possible.append((ny, nx, next_symbol, direction))
        if len(possible) == 0:
            return 0
        else:
            total = 0
            for vals in possible:
                total += check_full(*vals)
            return total
    else:
        ny, nx = y + direction[0], x + direction[1]
        if 0 <= nx < len(data) and 0 <= ny < len(data) and data[ny][nx] == next_symbol:
            return check_full(ny, nx, next_symbol, direction)
        else:
            return 0
 
total = 0

for y, x in starts:
    total += check_full(y, x, "X")
    
print(total)