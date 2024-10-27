# 숨바꼭질 4

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
MAX = 100000


def BFS():
    dist = [0] * (MAX + 1)  # 걸리는 시간
    move = [0] * (MAX + 1)  # 이전 노드
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            print(dist[x])
            arr = []
            temp = x
            for _ in range(dist[x] + 1):
                arr.append(temp)
                temp = move[temp]
            print(' '.join(map(str, arr[::-1])))
            return

        for nx in (x + 1, x - 1, x * 2):
            if 0 <= nx < MAX + 1 and dist[nx] == 0:
                dist[nx] = dist[x] + 1
                move[nx] = x
                q.append(nx)


BFS()
