from collections import defaultdict


def part_one(inp):
    card_sums = defaultdict(lambda: 0.5)

    for x, game in enumerate(inp):
        win_nums = {int(num) for num in game[10:40].split()}
        hand_nums = {int(num) for num in game[42:].split()}

        for _ in range(len(win_nums & hand_nums)):
            card_sums[x] *= 2

    return sum(int(val) for val in card_sums.values())


def part_two(inp):
    won_cards = defaultdict(lambda: 1)

    for x, game in enumerate(inp):
        win_nums = {int(num) for num in game[10:40].split()}
        hand_nums = {int(num) for num in game[42:].split()}

        for y in range(x + 1, x + len(hand_nums & win_nums) + 1):
            won_cards[y] += won_cards[x]
    
    return sum(won_cards.values())


def main():
    with open('input.txt', 'r') as f:
        content = [line.strip() for line in f]
    
    print(part_one(content))
    print(part_two(content))


main()