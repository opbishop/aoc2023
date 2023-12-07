import collections
import os
from functools import cmp_to_key

from common.common import get_input

cwd = os.getcwd()
c = get_input(cwd)

card_order = "A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J".replace(' ', '').split(',')
hands = {line.split()[0]: int(line.split()[1]) for line in c}

def score_hand(hand):
    if 'J' in hand:
        if all(c == 'J' for c in hand):
            hand = 'AAAAA'
        else:
            hand = hand.replace('J', max(set(hand.replace('J', '')), key=hand.count))
    c = collections.Counter(hand)
    counts = sorted(c.values(), reverse=True)
    if counts[0] == 5:
        return 7 #5 of a kind
    if counts[0] == 4:
        return 6 #4 of a kind
    if counts[0] == 3 and counts[1] == 2:
        return 5 #full house
    if counts[0] == 3:
        return 4 #3 of a kind
    if counts[0] == 2 and counts[1] == 2:
        return 3 #2 pair
    if counts[0] == 2:
        return 2 #one pair
    return 1 #high card

def compare(hand1, hand2):
    scores = (score_hand(hand1), score_hand(hand2))
    if scores[0] > scores[1]:
        print(f"{hand1} beats {hand2}")
        return 1
    elif scores[0] < scores[1]:
        print(f"{hand2} beats {hand1}")
        return -1

    for i in range(len(hand1)):
        card1, card2 = hand1[i], hand2[i]
        if card_order.index(card1) < card_order.index(card2):
            return 1
        if card_order.index(card1) > card_order.index(card2):
            return -1
    return 0

h_sorted = sorted(hands.keys(), key=cmp_to_key(compare))

s = 0
for idx, hand in enumerate(h_sorted):
    s += (idx + 1)*hands[hand]
print(s)
