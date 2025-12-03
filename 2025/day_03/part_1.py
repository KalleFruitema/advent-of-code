with open("input.txt") as file:
    data = [tuple(map(int, list(line.strip()))) 
            for line in file if line.strip() != ""]
    

jolts = []

for line in data:
    m = max(line[:-1])
    mloc = line.index(m)
    m2 = max(line[mloc+1:])
    jolts.append(int(f"{m}{m2}"))

print(sum(jolts))