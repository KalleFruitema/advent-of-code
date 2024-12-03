import re


with open("2024/day_03/input.txt") as file:
    data = file.read().strip()

result = re.findall(r"(do(?:n\'t)?)\(\)|mul\((\d+),(\d+)\)", data)

total = 0
enable = "do"

for i in result:
    if i[0]:
        enable = i[0]
    elif enable == "do":
        total += int(i[1]) * int(i[2])

print(total)
