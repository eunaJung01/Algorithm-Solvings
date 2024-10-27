# 카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

N = int(input().strip())

cards = [int(input().strip()) for _ in range(N)]
heapq.heapify(cards)

result = 0
while len(cards) >= 2:
    add = heapq.heappop(cards) + heapq.heappop(cards)
    result += add
    heapq.heappush(cards, add)

print(result)
