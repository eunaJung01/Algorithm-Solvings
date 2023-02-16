# 보석 도둑

import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []  # 우선순위 큐 : 무게 낮은 순
for _ in range(N):
    heapq.heappush(jewels, list(map(int, input().split())))

bags = [int(input().strip()) for _ in range(K)]
bags.sort()

steal = 0
costs = []  # 우선순위 큐 : 가격 높은 순
for bag in bags:
    while jewels and jewels[0][0] <= bag:
        heapq.heappush(costs, -heapq.heappop(jewels)[1])
    if costs:
        steal += abs(heapq.heappop(costs))
print(steal)
