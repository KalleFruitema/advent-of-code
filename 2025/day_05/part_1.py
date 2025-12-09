with open("input.txt") as file:
    ranges, ingredients = file.read().strip().split("\n\n")
    ranges = [tuple(map(int, i.split("-"))) for i in ranges.strip().split("\n")]
    ingredients = [int(i) for i in ingredients.strip().split("\n")]

count = 0

for ingredient in ingredients:
    for lower, upper in ranges:
        if lower <= ingredient <= upper:
            count += 1
            break
    

print(count)

