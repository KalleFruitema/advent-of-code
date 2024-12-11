from collections import defaultdict
from functools import lru_cache


@lru_cache
def times_2024(number: int):
    return number * 2024


@lru_cache
def half_split_string(text: str):
    halfway = len(text) >> 1
    return int(text[:halfway]), int(text[halfway:])


# seen = defaultdict(lambda: [])
@lru_cache
def calculate_stones(num: int, i):
    # seen[blinks+1-i].append(num)
    if i == 0:
        return 1
    if num == 0:
        return calculate_stones(1, i - 1)
    elif not len(s_num := str(num)) & 1:
        left, right = half_split_string(s_num)
        return calculate_stones(left, i - 1) + calculate_stones(right, i - 1)
    else:
        return calculate_stones(times_2024(num), i - 1)


blinks = 75



# for i in range(1, blinks + 1):
#     print(calculate_stones(0, i))

# for i, nums in seen.items():
#     print(f"\niter {i}\tlength {len(nums)}\n{' '.join(map(str, nums))}")