from pprint import pprint
from Location import Location


with open("2023/dag_10/input_test1.txt") as file:
    grid = [list(line.strip("\n")) for line in file]

for y, line in enumerate(grid):
    n_line = []
    for x, element in enumerate(line):
        n_line.append(Location((y, x), element))
    grid[y] = n_line

for y, line in enumerate(grid):
    for x, element in enumerate(line):
        if element.symbol == "S":
            start = element
            break

# surrounding = [(grid[y][x], (y, x)) for y in range(start[0] - 1, start[0] + 2)
#                for x in range(start[1] - 1, start[1] + 2) if (y, x) != start]

top = grid[start.location[0] - 1][start.location[1]]
right = grid[start.location[0]][start.location[1] + 1]
left = grid[start.location[0]][start.location[1] - 1]
bottom = grid[start.location[0] + 1][start.location[1]]

n_pos = []
if top.symbol in "|7F":
    n_pos.append(top)
if right.symbol in "-7J":
    n_pos.append(right)
if left.symbol in "-LF":
    n_pos.append(left)
if bottom.symbol in "|LJ":
    n_pos.append(bottom)

count = 0
all_pos = [start, *n_pos.copy()]
# pprint(n_pos)
pprint(grid)
print(type(n_pos[0]))
print(type(start))
print(start == start)
while n_pos[0] != n_pos[1]:
    print(type(n_pos[0]))
    nn_pos = []
    for location in n_pos:
        loc, pipe = location.get()
        if pipe == '-':
            possible = 
            for i in range(-1, 2, 2):
                if (n_loc := Location((loc[0], loc[1] + i), grid[loc[0]][loc[1] + i])) not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == '|':
            for i in range(-1, 2, 2):
                if (n_loc := Location((loc[0] + i, loc[1]), grid[loc[0] + i][loc[1]])) not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "F":
            possible = (Location((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        Location((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "7":
            possible = (Location((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        Location((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "J":
            possible = (Location((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        Location((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "L":
            possible = (Location((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        Location((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
    count += 1
    print("NIEUW", nn_pos)
    all_pos.extend(nn_pos)
    n_pos = nn_pos.copy()
count += 1


pprint(count)
