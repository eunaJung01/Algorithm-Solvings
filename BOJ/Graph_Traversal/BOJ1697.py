# 숨바꼭질

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
line = [False for _ in range(100001)]
result = 0

dx = [-1, 1]


def BFS(N):
    line[N] = True
    q = deque()
    q.append((N, 0))

    while q:
        cur, num = q.popleft()
        if cur == K:
            return num

        num += 1
        for i in range(3):
            if i == 2:
                x = cur * 2
            else:
                x = cur + dx[i]
            if 0 <= x < len(line) and not line[x]:
                q.append((x, num))
                line[x] = True


if N != K:
    result = BFS(N)
print(result)
