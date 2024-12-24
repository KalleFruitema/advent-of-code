a = int("110" + "101", 2)
b = 0
c = 0

while True:
    print(a, end=" ")
    b = a % 8
    b = b ^ 3
    c = a >> b
    a = a >> 3
    b = b ^ 5
    b = b ^ c
    print(b % 8)
    if a == 0:
        break
