from collections import defaultdict
from hashlib import sha256
from heapq import heappop, heappush
from time import perf_counter


with open("2024/day_19/input.txt") as file:
    available, designs = file.read().strip().split("\n\n")
    available = [i.strip() for i in available.strip().split(",")]
    designs = [i.strip() for i in designs.strip().split("\n")]


first_letter = defaultdict(lambda: [])
for pattern in available:
    first_letter[pattern[0]].append(pattern)
    
    
def complete_design(design):
    pq = [(0, "", "")]
    seen = {(0, "", "")}
    possible = 0
    while pq:
        cur_length, current, segments = heappop(pq)
        
        if cur_length == len(design):
            possible += 1
            continue
        
        i = len(current)
        char = design[i]

        for pattern in first_letter[char]:
            if cur_length + len(pattern) > len(design):
                continue
            for i2, a_char in enumerate(pattern):
                if design[i + i2] != a_char:
                    break
            else:
                new = current + pattern
                new_segments = f"{segments},{pattern}"
                if (len(new), new, new_segments) not in seen:
                    heappush(pq, (len(new), new, new_segments))
                    seen.add((len(new), new, new_segments))
                    
    return possible


total = 0
t1 = perf_counter()
for i, design in enumerate(designs):
    a = complete_design(design)
    total += a
    print(f"{i}: {a}")
    print(f"Time elapsed: {round(perf_counter() - t1, 2)}s")
    
print(total)