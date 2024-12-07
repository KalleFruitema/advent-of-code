from operator import add, mul, concat


with open("2024/day_07/input.txt") as file:
    data = [line.strip().split(":") for line in file if line.strip() != ""]


operators = (
    add, mul,
    lambda pos, val: int(concat(str(pos), str(val)))
)

total = 0

for ans, vals in data:
    ans = int(ans.strip())
    vals = tuple(map(int, vals.strip().split()))
    
    possible = set([int(vals[0])])
    for val in vals[1:]:
        possible = {o(pos, val) for pos in possible for o in operators}
    
    if ans in possible:
        total += ans
        
print(total)