with open("2024/day_11/input.txt") as file:
    data = list(map(int, file.read().strip().split()))

blinks = 25


def new_stones(stones: list[int]):
    i = 0
    while i < len(stones):
        num = stones[i]
        if num == 0:
            stones[i] = 1
        elif not len(s_num := str(num)) & 1:
            halfway = len(s_num) >> 1
            left, right = s_num[:halfway], s_num[halfway:]
            stones[i] = int(left)
            stones.insert(i + 1, int(right))
            i += 1
        else:
            stones[i] *= 2024
        i += 1
    return stones


for _ in range(blinks):
    data = new_stones(data)
    
print(len(data))