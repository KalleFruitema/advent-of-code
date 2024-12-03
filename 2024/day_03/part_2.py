import re


with open("2024/day_03/input.txt") as file:
    data = file.read().strip()

result = re.findall(r"(do(?:n\'t)?)\(\)|mul\((\d+),(\d+)\)", data)

total = 0

enable = True
for i in result:
    if i[0] == "do":
        enable = True
    elif i[0] == "don\'t":
        enable = False
    elif enable:
        total += int(i[1]) * int(i[2])

print(total)