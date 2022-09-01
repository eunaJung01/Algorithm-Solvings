# 격자상의 경로

import sys

N, M, K = map(int, sys.stdin.readline().split())
result = 0

dp = [[0 for _ in range(M)] for _ in range(N)]

if K == 0:
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
    result = dp[N - 1][M - 1]
else:
    ky, kx = (K - 1) // M, (K - 1) % M
    for i in range(ky + 1):
        for j in range(kx + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

    for i in range(ky, N):
        for j in range(kx, M):
            if i == ky and j == kx:
                continue
            if i == ky or j == kx:
                dp[i][j] = 1
            else:
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]

    result = dp[ky][kx] * dp[N - 1][M - 1]

print(result)
