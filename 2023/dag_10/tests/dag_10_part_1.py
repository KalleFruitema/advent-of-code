from pprint import pprint


with open("2023/dag_10/input.txt") as file:
    grid = [list(line.strip("\n")) for line in file]
    
for y, line in enumerate(grid):
    try:
        x = line.index("S")
        start = (y, x)
    except ValueError:
        pass

# surrounding = [(grid[y][x], (y, x)) for y in range(start[0] - 1, start[0] + 2)
#                for x in range(start[1] - 1, start[1] + 2) if (y, x) != start]

top = grid[start[0] - 1][start[1]]
right = grid[start[0]][start[1] + 1]
left = grid[start[0]][start[1] - 1]
bottom = grid[start[0] + 1][start[1]]

n_pos = []
if top in "|7F":
    n_pos.append(((start[0] - 1, start[1]), top))
if right in "-7J":
    n_pos.append(((start[0], start[1] + 1), right))
if left in "-LF":
    n_pos.append(((start[0], start[1] - 1), left))
if bottom in "|LJ":
    n_pos.append(((start[0] + 1, start[1]), bottom))

count = 0
all_pos = [(start, "S"), *n_pos.copy()]
while n_pos[0] != n_pos[1]:
    nn_pos = []
    for loc, pipe in n_pos:
        if pipe == '-':
            for i in range(-1, 2, 2):
                if (n_loc := ((loc[0], loc[1] + i), grid[loc[0]][loc[1] + i])) not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == '|':
            for i in range(-1, 2, 2):
                if (n_loc := ((loc[0] + i, loc[1]), grid[loc[0] + i][loc[1]])) not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "F":
            possible = (((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        ((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "7":
            possible = (((loc[0] + 1, loc[1]), grid[loc[0] + 1][loc[1]]),
                        ((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "J":
            possible = (((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        ((loc[0], loc[1] - 1), grid[loc[0]][loc[1] - 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
        elif pipe == "L":
            possible = (((loc[0] - 1, loc[1]), grid[loc[0] - 1][loc[1]]),
                        ((loc[0], loc[1] + 1), grid[loc[0]][loc[1] + 1]))
            for n_loc in possible:
                if n_loc not in all_pos:
                    nn_pos.append(n_loc)
    count += 1
    all_pos.extend(nn_pos)
    n_pos = nn_pos.copy()
count += 1


pprint(count)
