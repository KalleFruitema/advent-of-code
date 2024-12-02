import numpy as np
# from useful import *


with open("2024/day_02/input.txt") as file:
    data = [[int(i) for i in line.strip().split()] for line in file]


def check(report: list[int]):
    greater = True
    lesser = True
    wrong = False
    for i in range(1, len(report)):   
        if greater and report[i] > report[i - 1] and 1 <= abs(report[i] - report[i - 1]) <= 3:
            lesser = False
        elif lesser and report[i] < report[i - 1] and 1 <= abs(report[i] - report[i - 1]) <= 3:
            greater = False
        else:
            wrong = True
            
    return wrong


total = 0

for report in data:
    wrong = check(report)

    if wrong:
        for i in range(len(report)):
            temp = report.copy()
            temp.pop(i)
            wrong = check(temp)
            if not wrong:
                total += 1
                break
    else:
        total += 1
            
        
        
print(total)