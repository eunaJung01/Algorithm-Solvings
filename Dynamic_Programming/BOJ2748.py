# 피보나치 수 2

import sys

dp = [0 for _ in range(91)]
dp[0] = 0
dp[1] = 1

n = int(sys.stdin.readline().strip())
for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
print(dp[n])
