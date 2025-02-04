# 내리막 길

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def dfs(y, x):
    if y == N - 1 and x == M - 1:
        return 1
    if dp[y][x] > -1:
        return dp[y][x]

    dp[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if height[ny][nx] < height[y][x]:
            dp[y][x] += dfs(ny, nx)
    return dp[y][x]


print(dfs(0, 0))
