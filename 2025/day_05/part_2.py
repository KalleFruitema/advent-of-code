with open("input.txt") as file:
    ranges, _ = file.read().strip().split("\n\n")
    ranges = [tuple(map(int, i.split("-"))) for i in ranges.strip().split("\n")]


ranges = sorted(ranges, key=lambda x: x[0])

i = 0
while (i + 1) < len(ranges):
    s1, e1 = ranges[i]
    s2, e2 = ranges[i+1]
    
    if e1 >= s2:
        for _ in range(2):
            ranges.pop(i) 
        ranges.insert(i, (min(s1, s2), max(e1, e2)))
    else:
        i += 1

total = 0
for s, e in ranges:
    total += e - s + 1

print(total)