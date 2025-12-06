from functools import reduce
from operator import mul, add


with open("input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]
    operators = data.pop().split()
    nums_list = tuple(zip(*[map(int, line.split()) for line in data]))
    

total = 0

for operator, nums in zip(operators, nums_list):
    if operator == "*":
        total += reduce(mul, nums)
    else:
        total += reduce(add, nums)

print(total)