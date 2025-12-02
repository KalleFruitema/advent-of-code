with open("input.txt") as file:
    data = [tuple(map(int, r.split("-"))) for r in file.read().strip().split(",")]
    data = [range(i[0], i[1] + 1) for i in data]

invalid = []

for r in data:
    for i in r:
        y = str(i)
        if len(y) % 2 != 0:
            continue
        a = len(y) // 2
        if y[:a] == y[a:]:
            invalid.append(i)

print(sum(invalid))