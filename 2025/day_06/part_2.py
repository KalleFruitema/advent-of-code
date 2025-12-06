from functools import reduce
from operator import mul, add
import numpy as np


with open("input.txt") as file:
    data = [line for line in file if line.strip() != ""]
    operators = data.pop()
    nums_list = np.array([list(i) for i in data])

curr_nums = []
curr_op = operators[0]
total = 0

for i, op in enumerate(operators):
    if not op.isspace() and i != 0 or i == len(operators) - 1:
        nums = [int(num) for i in curr_nums if (num := ''.join(i).strip()) != '']
        if curr_op == "*":
            total += reduce(mul, nums)
        else:
            total += reduce(add, nums)
        
        curr_nums = [nums_list[:, i]]
        curr_op = op
    else:
        curr_nums.append(nums_list[:, i])

print(total)