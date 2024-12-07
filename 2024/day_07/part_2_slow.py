with open("2024/day_07/input.txt") as file:
    data = [line.strip().split(":") for line in file if line.strip() != ""]

total = 0

for ans, vals in data:
    ans = int(ans.strip())
    vals = vals.strip().split()
    
    possible = [int(vals[0])]
    for val in vals[1:]:
        n_possible = []
        for pos in possible:
            for o in "*+|":
                if o == "|":
                    n_possible.append(int(f"{pos}{val}"))
                else:
                    n_possible.append(eval(f"{pos} {o} {val}"))
        possible = n_possible.copy()
    
    if ans in possible:
        total += ans
        
print(total)