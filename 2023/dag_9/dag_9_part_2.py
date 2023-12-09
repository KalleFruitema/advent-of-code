import numpy as np


with open("2023/dag_9/input.txt", 'r') as file:
    content = np.array([[int(num) for num in line.strip().split(" ")] for line in file])
    

diff_content = []
for arr in content:
    diff_arrays = [arr]
    while True:
        arr = np.diff(arr)
        diff_arrays.append(arr)
        if not arr.any():
            break
    diff_content.append(diff_arrays)


totals = 0
for diff_arrays in diff_content:
    total = 0
    for diff_arr in diff_arrays[::-1]:
        total = diff_arr[0] - total
    totals += total
   
    
print(totals)