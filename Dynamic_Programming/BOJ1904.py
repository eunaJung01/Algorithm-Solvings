# 01타일

import sys

N = int(sys.stdin.readline().strip())

dp = [0 for _ in range(1000001)]
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = (dp[i - 2] + dp[i - 1]) % 15746
print(dp[N])
