from collections import defaultdict


with open("2024/day_05/input.txt") as file:
    rules, pages = file.read().strip().split("\n\n")
    left, right = (zip(*[rule.split("|") for rule in rules.split("\n")]))
    pages = [page.split(",") for page in pages.split("\n")]


before = defaultdict(lambda: set())

for first, last in zip(left, right):
    before[last].add(first)

page_nums = []

for i, page in enumerate(pages):
    after = set()
    for num in page[::-1]:
        if num not in after:
            if len(before[num] & after) == 0:
                after.add(num)
            else:
                break
            
    else:
        page_nums.append(int(page[len(page) // 2]))
        
print(sum(page_nums))