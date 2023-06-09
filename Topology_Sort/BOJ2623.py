# 음악프로그램

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int, input().split())
rules = defaultdict(list)
inDegrees = [0 for _ in range(N + 1)]

for _ in range(M):
    line = list(map(int, input().split()))
    for i in range(1, line[0]):
        singer, nextSinger = line[i], line[i + 1]
        rules[singer].append(nextSinger)
        inDegrees[nextSinger] += 1

q = deque()
for i in range(1, N + 1):
    if inDegrees[i] == 0:
        q.append(i)

orders = []
while q:
    singer = q.popleft()
    orders.append(singer)

    for nextSinger in rules[singer]:
        inDegrees[nextSinger] -= 1
        if inDegrees[nextSinger] == 0:
            q.append(nextSinger)

if len(orders) == N:
    for order in orders:
        print(order)
else:
    print(0)
