from collections import defaultdict


with open("2024/day_23/input.txt") as file:
    data = [line.strip().split("-") for line in file if line.strip() != ""]

connections = defaultdict(lambda: set())

for a, b in data:
    connections[a].add(b)
    connections[b].add(a)

networks = set()


def find_connection(comp, conns):
    current = tuple(sorted(conns))
    if current in networks:
        return
    networks.add(current)
    
    for comp2 in connections[comp]:
        if comp2 in conns or not conns <= connections[comp2]:
            continue
        find_connection(comp2, conns | {comp2})


for comp in connections.keys():
    find_connection(comp, {comp})

print(",".join(max(networks, key=len)))