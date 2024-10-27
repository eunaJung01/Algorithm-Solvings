# 알약

import sys

input = sys.stdin.readline

dp = [[0 for _ in range(31)] for _ in range(31)]
dp[0][1] = 1

for i in range(31):
    for j in range(i, 31):
        if i == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    n = int(input().strip())
    if n == 0:
        break
    print(dp[n][n])
