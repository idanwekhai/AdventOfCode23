from collections import Counter
with open('input.txt') as f:
    lines = [line.strip('\n').split(' ') for line in f]

strn_1 = "AKQJT98765432"
strn_2 = "AKQT98765432J"

def rank_cards(cards, lines, part):
    strn = strn_1 if part == 1 else strn_2
    total = 0
    tot_cards = len(lines)
    for _, hand_i in cards.items():
     sorted_hands = sorted(hand_i, key=lambda word: [strn.index(c) for c in word[0]])
     for h in range(len(sorted_hands)):
         total += sorted_hands[h][1]*tot_cards
         tot_cards-=1
    return total

def order_cards(cards, hand, bid, true_hand=None):
    if len(set(hand)) == 1:
        hand = hand if true_hand is None else true_hand
        cards['Five of a kind'].append([hand, int(bid)])
    elif set(Counter(hand).values()) == {1,4}:
        hand = hand if true_hand is None else true_hand
        cards['Four of a kind'].append([hand, int(bid)])
    elif set(Counter(hand).values()) == {2,3}:
        hand = hand if true_hand is None else true_hand
        cards['Full house'].append([hand, int(bid)])
    elif set(Counter(hand).values()) == {1,3}:
        hand = hand if true_hand is None else true_hand
        cards['Three of a kind'].append([hand, int(bid)])
    elif sorted(list(Counter(hand).values())) == [1,2,2]:
        hand = hand if true_hand is None else true_hand
        cards['Two pair'].append([hand, int(bid)])
    elif len(set(hand))  == 4:
        hand = hand if true_hand is None else true_hand
        cards['One pair'].append([hand, int(bid)])
    elif len(set(hand)) == 5:
        hand = hand if true_hand is None else true_hand
        cards['High card'].append([hand, int(bid)])

def part_1(lines):
    cards = {'Five of a kind': [],
           'Four of a kind': [],
           'Full house': [],
           'Three of a kind':[],
           'Two pair': [],
           'One pair': [],
           'High card': []}
    for hand, bid in lines:
        order_cards(cards, hand, bid)
    return rank_cards(cards, lines, 1)

def part_2(lines):
    cards = {'Five of a kind': [],
           'Four of a kind': [],
           'Full house': [],
           'Three of a kind':[],
           'Two pair': [],
           'One pair': [],
           'High card': []}
    for hand, bid in lines:
        if 'J' in hand:
            without_j = ''.join([i for i in list(hand) if i!='J'])
            if len(set(hand))==1:
                order_cards(cards, hand, bid)
            elif len(set(without_j)) == len(list(without_j)) and len(without_j)>2:
                high = sorted(without_j, key=lambda word: [strn_2.index(c) for c in word])[0]
                fake_hand = ''.join([i if i!='J' else high for i in list(hand)])
                order_cards(cards, fake_hand, bid, hand)
            else:
                mode_card = Counter(without_j).most_common(1)[0][0]
                fake_hand = ''.join([i if i!='J' else mode_card for i in list(hand)])
                order_cards(cards, fake_hand, bid, hand)
        else:
            order_cards(cards, hand, bid)
    return rank_cards(cards, lines, 2)

print(part_1(lines))
print(part_2(lines))