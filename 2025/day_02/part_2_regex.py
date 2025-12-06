from re import fullmatch


with open("input.txt") as file:
    data = [tuple(map(int, r.split("-"))) for r in file.read().strip().split(",")]
    data = [range(i[0], i[1] + 1) for i in data]

invalid = sum([i if fullmatch(r"(\d+)\1+", str(i)) else 0 for r in data for i in r])

print(invalid)