import re


with open("2024/day_03/input.txt") as file:
    data = file.read().strip()


result = re.findall(r'mul\((\d+),(\d+)\)', data)

total = 0

for num1, num2 in result:
    total += int(num1) * int(num2)

print(total)