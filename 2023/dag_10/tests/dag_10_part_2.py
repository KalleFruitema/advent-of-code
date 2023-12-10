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
print(start.get())
count = 0
all_pos = [start, *n_pos.copy()]
# pprint(n_pos)
# pprint(grid)
# print(type(n_pos[0]))
# print(type(start))
# print(start == start)


def compare(possible: tuple[Location, Location], all_pos: list[Location]):
    for n_loc in possible:
        for a_loc in all_pos:
            # print(n_loc.get()[0], a_loc.get()[0])
            if n_loc.get()[0] == a_loc.get()[0]:
                break
        else:
            return n_loc

pprint(grid)
while n_pos[0] != n_pos[1]:
    print(n_pos)
    nn_pos = []
    for location in n_pos:
        loc, pipe = location.get()
        if pipe == '-':
            possible = (Location((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]),
                        Location((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
        elif pipe == '|':
            possible = (Location((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        Location((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
        elif pipe == "F":
            possible = (Location((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        Location((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
        elif pipe == "7":
            possible = (Location((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        Location((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
        elif pipe == "J":
            possible = (Location((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        Location((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
        elif pipe == "L":
            possible = (Location((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        Location((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            f = compare(possible, all_pos)
            print(f)
            nn_pos.append(f)
    count += 1
    print("NIEUW", nn_pos)
    all_pos.extend(nn_pos)
    n_pos = nn_pos.copy()
count += 1


pprint(count)
