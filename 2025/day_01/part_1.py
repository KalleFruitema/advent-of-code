with open("input.txt") as file:
    data = [(line[0], int(line.strip()[1:])) for line in file if line.strip() != ""]

num = 50
count = 0

for dir, turns in data:
    if dir == "R":
        num = (num + turns) % 100
    else:
        num = (num - turns) % 100
    
    if num == 0:
        count += 1
        
print(count)