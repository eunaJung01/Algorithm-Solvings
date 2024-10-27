# 유기농 배추

import sys
from collections import deque

T = int(sys.stdin.readline().strip())

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def BFS(garden, cabbage, M, N):
    ans = 0

    for c in cabbage:
        q = deque([])
        if garden[c[1]][c[0]] == 1:
            garden[c[1]][c[0]] = 0
            ans += 1
            q.append(c)

            while q:
                x, y = q.pop()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and garden[ny][nx] == 1:
                        garden[ny][nx] = 0
                        q.append([nx, ny])
    return ans


result = []

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())  # NxM 배추밭, K개의 배추
    garden = [[0 for _ in range(M)] for _ in range(N)]

    cabbage = []  # x, y
    for i in range(K):
        cabbage.append(list(map(int, sys.stdin.readline().split())))
        garden[cabbage[i][1]][cabbage[i][0]] = 1

    result.append(BFS(garden, cabbage, M, N))

for r in result:
    print(r)
