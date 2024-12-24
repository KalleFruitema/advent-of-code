import re


with open("2024/day_22/input.txt") as file:
    initial = map(int, re.findall(r"\d+", file.read()))


def calculate_new_secret(secret):
    n_secret = ((secret * 64) ^ secret) % 16777216
    n_secret = (int(n_secret / 32) ^ n_secret) % 16777216
    n_secret = ((n_secret * 2048) ^ n_secret) % 16777216
    return n_secret


days = 2000
total = 0

for secret in initial:
    
    for i in range(days):
        secret = calculate_new_secret(secret)
    
    total += secret

print(total)