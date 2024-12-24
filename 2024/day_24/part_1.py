from collections import deque


with open("2024/day_24/input.txt") as file:
    sysvals, gates = file.read().strip().split("\n\n")

sysvals = [i.strip().split(": ") for i in sysvals.strip().split("\n")]
sysvals = {var: int(val) for var, val in sysvals}

gates = deque([i.strip().split(" ") for i in gates.split("\n")])

calc = {
    "AND": lambda a, b: a & b,
    "OR":  lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b
}

while gates:
    val1, op, val2, _, gate = gates.popleft()
    if val1 not in sysvals or val2 not in sysvals:
        gates.append([val1, op, val2, _, gate])
        continue
    sysvals[gate] = calc[op](sysvals[val1], sysvals[val2])

total = []

for k, v in sysvals.items():
    if k[0] == "z":
        total.append((k, str(v)))
        
total = "".join(map(lambda x: x[1], sorted(total, reverse=True)))

total = int(total, 2)
print(total)