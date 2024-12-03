with open("2024/day_02/input.txt") as file:
    data = [[int(i) for i in line.strip().split()] for line in file if line.strip() != ""]


total = 0

for report in data:
    greater = True
    lesser = True
    for i in range(1, len(report)):   
        if greater and report[i] > report[i - 1] and 1 <= abs(report[i] - report[i - 1]) <= 3:
            lesser = False
        elif lesser and report[i] < report[i - 1] and 1 <= abs(report[i] - report[i - 1]) <= 3:
            greater = False
        else:
            break
    else:
        total += 1
        
print(total)