from collections import defaultdict
from heapq import heappop, heappush


with open("2024/day_19/input.txt") as file:
    available, display = file.read().strip().split("\n\n")
    available = [i.strip() for i in available.strip().split(",")]
    display = [i.strip() for i in display.strip().split("\n")]


first_letter = defaultdict(lambda: [])
for pattern in available:
    first_letter[pattern[0]].append(pattern)
    
    
def complete_display(d_pattern):
    pq = [(0, "")]
    seen = {(0, "")}
    while pq:
        cur_length, current = heappop(pq)
        
        if cur_length == len(d_pattern):
            return True
        
        i = len(current)
        char = d_pattern[i]

        for pattern in first_letter[char]:
            if cur_length + len(pattern) > len(d_pattern):
                continue
            for i2, a_char in enumerate(pattern):
                if d_pattern[i + i2] != a_char:
                    break
            else:
                new = current + pattern
                if (len(new), new) not in seen:
                    heappush(pq, (len(new), new))
                    seen.add((len(new), new))
                    
    return False


total = 0
for i, d_pattern in enumerate(display):
    total += complete_display(d_pattern)
    
print(total)