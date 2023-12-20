from time import perf_counter


count = 0
t1 = perf_counter()
for i in range(1_000_000_000):
    count += 1
t2 = perf_counter()

print(t2-t1)