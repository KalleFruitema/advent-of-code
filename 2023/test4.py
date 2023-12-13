from pprint import pprint


def gprint(grid: list[list[str]]):
    print()
    for line in grid:
        print(" ".join(str(i) for i in line))
    print()


def transpose(mirror):
    return list(zip(*mirror))


lst = [[1, 2, 3],
       [4, 5, 6]]

gprint(lst)

x = transpose(lst)
gprint(x)

y = transpose(x)
gprint(y)

z = transpose(y)
gprint(z)