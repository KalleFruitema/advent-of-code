from pprint import pprint
import numpy as np


def input():
    with open("2023/dag_18/input.txt") as file:
        instructs = [line.strip().split(" ")[-1].strip("()#") for line in file]
    return instructs
       

def translate_instructs(instructs):
    n_instructs = []
    for instruct in instructs:
        n_instructs.append((int(instruct[:-1], 16), int(instruct[-1])))
    return n_instructs


def get_all_coords(instructs):
    x, y = 0, 0
    all_coords = [(0, 0)]
    boundary = 0
    for steps, direc in instructs:
        if direc == 0:
            x += steps
        elif direc == 1:
            y += steps
        elif direc == 2:
            x -= steps
        else:
            y -= steps
        boundary += steps
        all_coords.append((x, y))
    return all_coords, boundary


def pathArea(path):
    if len(path) < 3:
        return 0

    A = 0.0
    for i in range(0, len(path)):
        A += path[i-1][0] * path[i][1] - path[i][0] * path[i-1][1]

    return 0.5 * abs(A)


def pick(f, boundary):
    return f + boundary/2 + 1

    
def main():
    instructs = input()
    instructs = translate_instructs(instructs)
    all_coords, boundary = get_all_coords(instructs)
    f = pathArea(all_coords)
    answer = pick(f, boundary)
    print(answer)
    
    
if __name__ == "__main__":
    main()
