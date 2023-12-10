from pprint import pprint
from time import perf_counter


def print_grid(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(line))
    print()

t1 = perf_counter()
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

top_pos = (start[0] - 1, start[1])
right_pos = (start[0], start[1] + 1)
left_pos = (start[0], start[1] - 1)
bottom_pos = (start[0] + 1, start[1])

top = grid[top_pos[0]][top_pos[1]]
right = grid[right_pos[0]][right_pos[1]]
left = grid[left_pos[0]][left_pos[1]]
bottom = grid[bottom_pos[0]][bottom_pos[1]]

n_pos = []
n_start_possible = set(list("-|7FJL"))
if top in "|7F":
    n_pos.append(((start[0] - 1, start[1]), top))
    for char in "-7F":
        if char in n_start_possible:
            n_start_possible.remove(char)
if right in "-7J":
    n_pos.append(((start[0], start[1] + 1), right))
    for char in "J7|":
        if char in n_start_possible:
            n_start_possible.remove(char)
if left in "-LF":
    n_pos.append(((start[0], start[1] - 1), left))
    for char in "|FL":
        if char in n_start_possible:
            n_start_possible.remove(char)
if bottom in "|LJ":
    n_pos.append(((start[0] + 1, start[1]), bottom))
    for char in "-JL":
        if char in n_start_possible:
            n_start_possible.remove(char)
n_start = list(n_start_possible)[0]

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

t2 = perf_counter()

print("\n-------------PART 1---------------\n")

print(count)
print(f"\nTook {t2-t1} seconds.")

print("\n-------------PART 2---------------\n")

t3 = perf_counter()

n_grid = []
for y, line in enumerate(grid):
    n_line = []
    for x, element in enumerate(line):
        if ((y, x), element) in all_pos:
            n_line.append(element)
        else:
            n_line.append("O")
    n_grid.append(n_line)
    
n_grid[start[0]][start[1]] = n_start

def count_crossovers_hor(side: list[str]):
    on_pipe = ""
    crossovers = 0
    for char in side:
        if char == "|":
            crossovers += 1
        elif char in "FL":
            on_pipe = char
        elif char in "7J" and on_pipe:
            if char == "J" and on_pipe == "F" or\
                char == "7" and on_pipe == "L":
                    crossovers += 1
            on_pipe = ""
    return crossovers


def count_crossovers_vert(side: list[str]):
    on_pipe = ""
    crossovers = 0
    for char in side:
        if char == "-":
            crossovers += 1
        elif char in "F7":
            on_pipe = char
        elif char in "LJ" and on_pipe:
            if char == "L" and on_pipe == "7" or\
                char == "J" and on_pipe == "F":
                    crossovers += 1
            on_pipe = ""
    return crossovers


for y, line in enumerate(n_grid):
    for x, element in enumerate(line):
        if element != "O":
            continue
        
        horizontal = line.copy()
        vertical = [n_grid[i][x] for i in range(len(n_grid))]
        leftside, rightside = horizontal[:x], horizontal[x + 1:]
        topside, botside = vertical[:y], vertical[y + 1:]
   
        crossovers = []
        crossovers.append(count_crossovers_hor(rightside))
        crossovers.append(count_crossovers_hor(leftside))
        crossovers.append(count_crossovers_vert(topside))
        crossovers.append(count_crossovers_vert(botside))
        # print(crossovers)
        if all([i % 2 == 1 for i in crossovers]):
            n_grid[y][x] = "I"
            
i_count = 0
for y, line in enumerate(n_grid):
    for x, element in enumerate(line):
        if element == "I":
            i_count += 1
            # print(y, x)

t4 = perf_counter()

print(i_count)
print(f"\nTook {t4-t3} seconds.\n")
