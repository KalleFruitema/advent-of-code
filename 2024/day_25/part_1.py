from pprint import pprint


with open("2024/day_25/input.txt") as file:
    data = [i.strip().split("\n") for i in file.read().strip().split("\n\n")]

locks = []
keys = []

for i in data:
    if all(x == "#" for x in i[0]):
        locks.append(i)
    else:
        keys.append(i)

lock_heights = []

for lock in locks:
    heights = []
    for col in tuple(zip(*lock)):
        for y, val in enumerate(col):
            if val != "#":
                heights.append(y - 1)
                break
    lock_heights.append(heights)
    
key_heights = []
for key in keys:
    heights = []
    for col in tuple(zip(*key)):
        for y, val in enumerate(col):
            if val == "#":
                heights.append(y)
                break
    key_heights.append(heights)

total = 0

for lock in lock_heights:
    for key in key_heights:
        for l, k in zip(lock, key):
            if l >= k:
                break
        else:
            total += 1

print(total)