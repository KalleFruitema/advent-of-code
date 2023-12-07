from collections import defaultdict
from pprint import pprint
from copy import deepcopy
from itertools import groupby


with open("2023/dag_7/input.txt", 'r') as file:
    hands = [line.strip().split(" ") for line in file]
    

def identify_class(hand):
    card_dict = defaultdict(lambda: 0)
    for card in hand[0]:
        card_dict[card] += 1
    
    if len(card_dict) == 1:
        return 7
    elif len(card_dict) == 2:
        for num in card_dict.values():
            if num == 4:
                return 6
        else:
            return 5
    elif len(card_dict) == 3:
        for num in card_dict.values():
            if num == 3:
                return 4
        else:
            return 3
    elif len(card_dict) == 4:
        return 2
    else:
        return 1


def identify_cardscore(card):
    check = list("AKQJT98765432")
    return [check.index(char) for char in card[0]]


def sort_group(group):
    return sorted(group, key=identify_cardscore)
        
    
for i, hand in enumerate(hands):
    hand.append(identify_class(hand))

hands.sort(key=lambda x: x[2], reverse=True)

grouped_hands = []
for i, l in (groupby(hands, lambda x: x[2])):
    grouped_hands.append(list(l))
    
# pprint(grouped_hands)
order_lst = []
for group in grouped_hands:
    sorted_group = sort_group(group)
    order_lst.extend([*sorted_group])

print()

total = 0
for i, card in enumerate(order_lst[::-1], start=1):
    total += int(card[1]) * i
    
print(total)