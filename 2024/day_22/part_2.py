from collections import defaultdict, deque
import re
from time import perf_counter
import numpy as np


t1 = perf_counter()

with open("2024/day_22/input.txt") as file:
    initial = map(int, re.findall(r"\d+", file.read()))


def calculate_new_secret(secret):
    n_secret = ((secret * 64) ^ secret) % 16777216
    n_secret = (int(n_secret / 32) ^ n_secret) % 16777216
    n_secret = ((n_secret * 2048) ^ n_secret) % 16777216
    return n_secret


days = 2000
all_prices = []

for secret in initial:
    prices = [int(str(secret)[-1])]
    for i in range(days):
        secret = calculate_new_secret(secret)
        prices.append(int(str(secret)[-1]))
    all_prices.append(prices)

all_price_diffs = []
totals = defaultdict(lambda: 0)

for prices in all_prices:
    diffs = np.diff(prices)
    window = deque(diffs[:4])
    totals[tuple(window)] += prices[4]
    seen = {tuple(window)}
    
    for i in range(4, len(diffs)):
        window.popleft()
        window.append(diffs[i])
        if (hashable := tuple(window)) not in seen:
            totals[hashable] += prices[i + 1]
            seen.add(hashable)
            
print(max(totals.items(), key=lambda x: x[1]))
