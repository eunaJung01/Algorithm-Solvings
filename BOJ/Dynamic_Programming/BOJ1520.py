# 내리막 길

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
altitude = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def DFS(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M and altitude[ny][nx] < altitude[y][x]:
            dp[y][x] += DFS(ny, nx)
    return dp[y][x]


dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[N - 1][M - 1] = 1
print(DFS(0, 0))
