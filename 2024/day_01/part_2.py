from collections import Counter
import numpy as np
from useful import *


with open("2024/day_01/test_input.txt") as file:
    data = [line.strip() for line in file if line.strip() != ""]

left, right = map(list, zip(*[map(int, line.split()) for line in data]))

c = Counter(right)

total2 = 0

for num in left:
    total2 += num * c[num]
    
print(total2)