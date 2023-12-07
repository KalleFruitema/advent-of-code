from functools import reduce
from pprint import pprint
import numpy as np


def content_one():
    with open(r'2023/dag_6/input.txt') as file:
        content = np.array([[int(x) for x in line.split(":")[1].strip().split()] 
                for line in file]).swapaxes(1, 0)
    return content


def content_two():
    with open(r'2023/dag_6/input.txt') as file:
        content = [[int(line.split(":")[1].replace(" ", '')) for line in file]]
    return content


def part_one(content):
    full_possibilities = 1
    for time, dist_record in content:
        record_possibilities = 0
        for speed in range(time):
            dist = (time - speed) * speed
            if dist > dist_record:
                record_possibilities += 1
        full_possibilities *= record_possibilities
    return full_possibilities


def part_two(content):
    return part_one(content)
    

total1 = part_one(content_one())
print(total1)

total2 = part_two(content_two())
print(total2)