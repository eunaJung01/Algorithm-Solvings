# RGB 거리

import sys

N = int(sys.stdin.readline().strip())
dp = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # n번째 집을 m색으로 칠했을 때 최솟값 (R : 0, G : 1, B : 2)

for i in range(1, N):
    dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] += min(dp[i - 1][2], dp[i - 1][0])
    dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

print(min(dp[N - 1]))
