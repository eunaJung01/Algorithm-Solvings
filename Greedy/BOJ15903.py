# 카드 합체 놀이

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))

for _ in range(m):
    card.sort()
    min_score = card[0] + card[1]
    card[0] = min_score
    card[1] = min_score

print(sum(card))
