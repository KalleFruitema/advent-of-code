from functools import cache


with open("2024/day_19/input.txt") as file:
    available, designs = file.read().strip().split("\n\n")
    available = set([i.strip() for i in available.strip().split(",")])
    designs = [i.strip() for i in designs.strip().split("\n")]

    
@cache
def count_combos(design) -> int:
    if not design:
        return 1
    
    combos = 0
    for pattern in available:
        if design.startswith(pattern):
            combos += count_combos(design[len(pattern):])
            
    return combos


total = sum(count_combos(design) for design in designs)
print(total)