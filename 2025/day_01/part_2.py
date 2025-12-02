with open("input.txt") as file:
    data = [(line[0], int(line.strip()[1:])) for line in file if line.strip() != ""]

num = 50
count = 0

for dir, turns in data:
    zeroes = 0
    
    zeroes += turns // 100
    new_turns = turns - ((turns // 100) * 100)
    
    if dir == "R":
        new_num = (num + new_turns) % 100
        if new_turns >= (100 - num) and num != 0:
            zeroes += 1
        
    else:
        new_num = (num - new_turns) % 100
        if new_turns >= num and num != 0:
            zeroes += 1
    
    num = new_num    
    count += zeroes


print(count)