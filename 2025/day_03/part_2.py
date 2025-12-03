with open("input.txt") as file:
    data = [tuple(map(int, list(line.strip()))) 
            for line in file if line.strip() != ""]
    
jolts = []

for line in data:
    m = max(line[:-11])
    mloc = line.index(m)
    jolt = f"{m}"
    
    for i in range(10, -1, -1):
        if i == 0:
            jolt += str(max(line[mloc+1:]))
            break
        
        m = max(line[mloc+1:-i])
        mloc = mloc + line[mloc+1:-i].index(m) + 1
        jolt += str(m)
        
    jolts.append(int(jolt))

print(sum(jolts))