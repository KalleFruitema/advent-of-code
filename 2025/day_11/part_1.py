from collections import deque


with open("input.txt") as file:
    data = [line.strip().split(":") for line in file if line.strip()]
    
edges = {}
for start, ends in data:
    edges[start.strip()] = tuple(i.strip() for i in ends.split())


pq = deque(["you"])
count = 0

while pq:
    node = pq.popleft()

    if node == "out":
        count += 1
        continue
    
    for n_node in edges[node]:
        pq.append(n_node)

print(count)