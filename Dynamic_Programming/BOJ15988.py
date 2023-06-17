# 1, 2, 3 더하기 3

import sys

input = sys.stdin.readline

T = int(input().strip())

cases = [int(input().strip()) for _ in range(T)]

dp = [0 for _ in range(max(cases) + 1)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, max(cases) + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

for n in cases:
    print(dp[n])
