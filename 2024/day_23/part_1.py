from collections import defaultdict


with open("2024/day_23/input.txt") as file:
    data = [line.strip().split("-") for line in file if line.strip() != ""]

connections = defaultdict(lambda: set())

for a, b in data:
    connections[a].add(b)
    connections[b].add(a)

triple_sets = set()

for k, v in connections.items():
    for y in v.copy():
        v.remove(y)
        for t in connections[y] & v:
            if "t" in [k[0], y[0], t[0]]:
                triple_sets.add(tuple(sorted([k, y, t])))

print(len(triple_sets))