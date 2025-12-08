from functools import reduce
import math
from collections import defaultdict, deque


with open("input.txt") as file:
    boxes = [tuple(map(int, line.strip().split(","))) for line in file if line.strip()]
    
distances = []

for i, (x1, y1, z1) in enumerate(boxes):
    for i2, (x2, y2, z2) in enumerate(boxes[i+1:], start=i+1):
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
        distances.append(((i, i2), distance))

pairs = [set(i[0]) for i in sorted(distances, key=lambda x: x[1])]
nodes = reduce(set.union, pairs)

for i in range(len(boxes), len(pairs) - 1):
    curr_pairs = pairs[:i]
    latest = curr_pairs[-1]
    edges = defaultdict(lambda: set())

    for a, b in curr_pairs:
        edges[a].add(b)
        edges[b].add(a)

    seen = set()
    pq = deque(list(nodes)[:1])
    
    while pq:
        node = pq.popleft()
        if node in seen:
            continue
        seen.add(node)
        
        for next in edges[node]:
            if next in seen:
                continue
            pq.append(next)
         
    if len(seen) == len(nodes):
        break
else:
    raise BrokenPipeError

print(reduce(int.__mul__, [boxes[i][0] for i in latest]))
