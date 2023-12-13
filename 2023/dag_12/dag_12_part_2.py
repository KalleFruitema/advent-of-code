from pprint import pprint
from more_itertools import distinct_permutations


def print_grid(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(line))
    print()


with open("2023/dag_12/input_test1.txt") as file:
    content = [line.strip() for line in file]
    

grid, instructs = [], []
for line in content:
    line = line.split(" ")
    grid.append(list(line[0]))
    instructs.append([int(i) for i in line[1].split(",")])


def check_if_valid(old_line, check_line: tuple, instruc):
    count = 0
    for i, char in enumerate(old_line):
        if char == "?":
            old_line[i] = check_line[count]
            count += 1
    n_line = [len(i) for i in "".join(old_line).split(".") if i != ""]
    return n_line == instruc


all_possible = []
total_count = 0
c = 1
for line, instruc in zip(grid, instructs):
    unfolded = list("?".join(["".join(line) for _ in range(5)]))
    unfold_instruc = instruc * 5
    leftover = sum(unfold_instruc) - unfolded.count("#")
    x = unfolded.count("?")
    to_input = []
    for _ in range(x):
        if leftover:
            to_input.append("#")
            leftover -= 1
        else:
            to_input.append(".")
    possible = distinct_permutations(to_input)
    line_count = 0
    # for possibility in possible:
    #     if check_if_valid(unfolded.copy(), possibility, unfold_instruc):
    #         line_count += 1
    print(f"{c}: {line_count}")
    c += 1
    total_count += line_count
    

print(total_count)