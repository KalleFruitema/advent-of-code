with open("2024/day_04/input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

starts = []
diagonal_pairs = {
    (-1,-1): (1,1), 
    (-1,1): (1, -1)
}
opposite_char = {
    "M": "S",
    "S": "M"
}
total = 0

for y, row in enumerate(data):
    for x, val in enumerate(row):
        if val == "A":
            crossing = 0
            for direction in diagonal_pairs.keys():
                ny, nx = y + direction[0], x + direction[1]
                opposite_direction = diagonal_pairs[direction]
                oy, ox = y + opposite_direction[0], x + opposite_direction[1]
                if 0 <= nx < len(data) and 0 <= ny < len(data) and (char := data[ny][nx]) in "MS":
                    if 0 <= ox < len(data) and 0 <= oy < len(data) and data[oy][ox] == opposite_char[char]:
                        crossing += 1
            if crossing == 2:
                total += 1

print(total)