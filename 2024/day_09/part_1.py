from collections import deque


with open("2024/day_09/input.txt") as file:
    data = deque(map(int, file.read().strip()))

data2 = deque(int(i / 2) for i, num in enumerate(data) for _ in range(num) if i / 2 == int(i / 2))
n_data = []

for i, num in enumerate(data):
    if i % 2 == 0:
        n_data.extend(data2.popleft() for _ in range(num) if data2)
    else:
        n_data.extend(data2.pop() for _ in range(num) if data2)
    
    
total = sum(i * num for i, num in enumerate(n_data))

print(total)