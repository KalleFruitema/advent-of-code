from functools import lru_cache


with open("input.txt") as file:
    data = [line.strip().split(":") for line in file if line.strip()]
    
edges = {}
for start, ends in data:
    edges[start.strip()] = tuple(i.strip() for i in ends.split())


@lru_cache
def count_paths(node, end):
    if node == end:
        return 1

    total = 0
    for n_node in edges.get(node, []):
        total += count_paths(n_node, end)
    return total


if count_paths("fft", "dac"):
    paths = count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
else:
    paths = count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")

print(paths)