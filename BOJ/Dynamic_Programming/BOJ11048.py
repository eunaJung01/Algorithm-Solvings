# 이동하기

import sys

N, M = map(int, sys.stdin.readline().split())
candy = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(M)] for _ in range(N)]

dy = (1, 0, 1)
dx = (0, 1, 1)

dp[0][0] = candy[0][0]

for i in range(N):
    for j in range(M):
        y = i
        x = j
        for k in range(3):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                dp[ny][nx] = max(dp[ny][nx], dp[y][x] + candy[ny][nx])

print(dp[N - 1][M - 1])
