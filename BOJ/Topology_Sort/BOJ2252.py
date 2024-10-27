# 줄 세우기

import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

queue = deque([])
cnt = defaultdict(int)  # 집입 차수
connect = defaultdict(list)  # 간선 정보들

for _ in range(M):
    A, B = map(int, input().split())
    cnt[B] += 1
    connect[A].append(B)

for i in range(1, N + 1):
    if cnt[i] == 0:
        queue.append(i)

answer = []
while queue:
    node = queue.popleft()
    answer.append(node)

    for n in connect[node]:
        cnt[n] -= 1
        if cnt[n] == 0:
            queue.append(n)

print(' '.join(map(str, answer)))
