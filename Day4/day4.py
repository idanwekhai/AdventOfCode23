import re
from collections import defaultdict
with open('Day4/input.txt') as f:
  cards = [line.strip('\n') for line in f]

def prob_1(cards):
    total_points = 0
    for card in cards:
        point = 0
        card_nums = card.split(':')[1]
        card_nums = card_nums.split('|')
        winning_nums = list(map(int, re.findall(r'\d+', card_nums[0])))
        nums_i_have = list(map(int, re.findall(r'\d+', card_nums[1])))
        for num in winning_nums:
            if num in nums_i_have:
                if point == 0:
                    point += 1
                else:
                    point = point * 2
        total_points += point
    return total_points

def prob_2(cards):
    card_tracker = defaultdict(int)
    for card in cards:
        card_nums = card.split(':')[1]
        card_num = int(re.findall(r'\d+', card.split(':')[0])[0])
        card_nums = card_nums.split('|')
        winning_nums = set(map(int, re.findall(r'\d+', card_nums[0])))
        nums_i_have = set(map(int, re.findall(r'\d+', card_nums[1])))
        num_matching_cards = len(winning_nums.intersection(nums_i_have))
        card_tracker[card_num] += 1
        for _ in range(card_tracker[card_num]):
            for i in range(1, num_matching_cards+1):
                card_tracker[card_num+i] += 1
    return sum(card_tracker.values())

print(prob_1(cards))
print(prob_2(cards))