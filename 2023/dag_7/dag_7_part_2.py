from collections import defaultdict
from pprint import pprint
from copy import deepcopy
from itertools import groupby


with open("2023/dag_7/input.txt", 'r') as file:
    hands = [line.strip().split(" ") for line in file]
    

def identify_class(hand):
    card_dict = defaultdict(lambda: 0)
    for card in hand:
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
    check = list("AKQT98765432J")
    return [check.index(char) for char in card[0]]


def sort_group(group):
    return sorted(group, key=identify_cardscore)
        

def best_possible(hand):
    if "J" not in hand:
        return [hand, hand] 
    elif hand == "JJJJJ":
        n_hand = "99999"
    else:
        char_dict = defaultdict(lambda: 0)
        for char in hand:
            if char != "J":
                char_dict[char] += 1
        famous = max(char_dict.items(), key=lambda x: x[1])
        n_hand = hand.replace("J", famous[0])
    return [hand, n_hand]
 

for i, hand in enumerate(hands):
    hands[i] = [best_possible(hand[0]), hand[1]]

n_hands = []
for i, hand in enumerate(hands):
    n_hands.append([hand[0][0], hand[1], identify_class(hand[0][1])])

n_hands.sort(key=lambda x: x[2], reverse=True)

grouped_hands = []
for i, l in (groupby(n_hands, lambda x: x[2])):
    grouped_hands.append(list(l))
    
# pprint(grouped_hands)
order_lst = []
for group in grouped_hands:
    sorted_group = sort_group(group)
    order_lst.extend([*sorted_group])

total = 0
for i, card in enumerate(order_lst[::-1], start=1):
    total += int(card[1]) * i
    
print(total)