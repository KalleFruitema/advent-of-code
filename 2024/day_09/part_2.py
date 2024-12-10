from collections import deque


with open("2024/day_09/input.txt") as file:
    data = list(map(int, file.read().strip()))

data2 = [i for i in [[int(i / 2) if i / 2 == int(i / 2) else "." for _ in range(num)] for i, num in enumerate(data)] if i]

i = len(data2) - 1
seen = set()
while 0 <= i:
    l = data2[i]
    if l[0] != "." and tuple(l) not in seen:
        for i2, l2 in enumerate(data2):
            if i2 > i:
                break
            if l2[0] == "." and len(l2) >= len(l):
                remaining = ["." for _ in range(len(l2) - len(l))]
                data2[i], data2[i2] = ["." for _ in range(len(l))], l
                if remaining:
                    data2.insert(i2 + 1, remaining)
                    i += 1
                break
        seen.add(tuple(l))
    i -= 1

total = 0
for i, num in enumerate([num for l in data2 for num in l]):
    if num != ".":
        total += i * int(num)

print(total)