from pprint import pprint
import numpy as np


def input():
    with open("2023/dag_18/input.txt") as file:
        instructs = [line.strip().split(" ") for line in file]
    return instructs


def get_all_coords(instructs):
    x, y = 0, 0
    all_coords = [(0, 0)]
    boundary = 0
    for direc, steps, _ in instructs:
        if direc == "R":
            x += int(steps)
        elif direc == "D":
            y += int(steps)
        elif direc == "L":
            x -= int(steps)
        else:
            y -= int(steps)
        boundary += int(steps)
        all_coords.append((x, y))
    return all_coords, boundary
            

def shoelace_formula_3(x, y, absoluteValue = True):
    result = 0.5 * np.array(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    if absoluteValue:
        return abs(result)
    else:
        return result


def pick(f, boundary):
    return f + boundary/2 + 1

    
def main():
    instructs = input()
    all_coords, boundary = get_all_coords(instructs)
    x = [i[0] for i in all_coords]
    y = [i[1] for i in all_coords]
    f = shoelace_formula_3(x, y)
    answer = pick(f, boundary)
    print(answer)
    
    
if __name__ == "__main__":
    main()
