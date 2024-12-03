with open("2024/day_01/test_input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

left, right = map(list, zip(*[map(int, line.split()) for line in data]))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += abs(left[i] - right[i])
    
print(total)