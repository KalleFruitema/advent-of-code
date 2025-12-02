with open("input.txt") as file:
    data = [tuple(map(int, r.split("-"))) for r in file.read().strip().split(",")]
    data = [range(i[0], i[1] + 1) for i in data]

invalid = []

for r in data:
    for i in r:
        y = str(i)
        for split in range(1, len(y) // 2 + 1):
            if not (len(y) / split).is_integer():
                continue
            s = y[:split]
            for times in range(1, (len(y) // split)):
                if s != y[times * split:(times+1) * split]:
                    break
            else:
                invalid.append(i)
                break
            

print(sum(invalid))