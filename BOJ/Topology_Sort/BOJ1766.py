# 문제집

import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
inDegrees = [0 for _ in range(N + 1)]

rules = defaultdict(list)
for _ in range(M):
    A, B = map(int, input().split())  # A번 문제를 B번 문제보다 먼저 푸는 것이 좋다.
    rules[A].append(B)
    inDegrees[B] += 1

q = []
for i in range(1, N + 1):
    if inDegrees[i] == 0:
        heapq.heappush(q, i)

order = []
while q:
    num = heapq.heappop(q)
    order.append(num)

    for nextNum in rules[num]:
        inDegrees[nextNum] -= 1
        if inDegrees[nextNum] == 0:
            heapq.heappush(q, nextNum)

print(' '.join(map(str, order)))
