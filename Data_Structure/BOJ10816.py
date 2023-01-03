# 숫자 카드 2

import sys

input = sys.stdin.readline

N = input().strip()
cards = list(map(int, input().split()))
M = input().strip()
target_cards = list(map(int, input().split()))

card_nums = dict()
for c in cards:
    if c in card_nums:
        card_nums[c] += 1
    else:
        card_nums[c] = 1

result = []
for t in target_cards:
    if t not in card_nums:
        result.append(0)
    else:
        result.append(card_nums[t])

for r in result:
    print(r, end=' ')
