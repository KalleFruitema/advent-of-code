from functools import cache
from time import perf_counter


with open("2024/day_11/input.txt") as file:
    data = list(map(int, file.read().strip().split()))

blinks = 75


@cache
def times_2024(number: int):
    return number * 2024


@cache
def half_split_string(text: str):
    halfway = len(text) >> 1
    return int(text[:halfway]), int(text[halfway:])


@cache
def calculate_stones(num: int, i):
    if i == 0:
        return 1
    if num == 0:
        return calculate_stones(1, i - 1)
    elif not len(s_num := str(num)) & 1:
        left, right = half_split_string(s_num)
        return calculate_stones(left, i - 1) + calculate_stones(right, i - 1)
    else:
        return calculate_stones(times_2024(num), i - 1)

t1 = perf_counter()
total = 0

for stone in data:
    total += calculate_stones(stone, blinks)

print(total)
print(f"Took: {perf_counter() - t1} seconds")