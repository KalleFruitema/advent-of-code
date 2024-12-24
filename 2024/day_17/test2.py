from collections import defaultdict


numdict = defaultdict(lambda: [])
nums = [2,4,1,3,7,5,0,3,1,5,4,1,5,5,3,0]

for tmp in range(0, 8):
    a = tmp
    b = a % 8
    b = b ^ 3
    c = a >> b
    a = a >> 3
    b = b ^ 5
    b = b ^ c
    numdict[b % 8].append(bin(tmp)[2:])

print(numdict)

totals_bin = ""

def back_one(current: list[int], a_val):
    num = current.pop()
    for i in range(0, 8):
        a = bin(i)
        b = a % 8
        b = b ^ 3
        c = a >> b
        a = a >> 3
        b = b ^ 5
        b = b ^ c
        ans = b % 8