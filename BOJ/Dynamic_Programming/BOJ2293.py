# 동전 1

import sys

n, k = map(int, sys.stdin.readline().split())
price = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    for j in range(price[i], k + 1):
        dp[j] += dp[j - price[i]]

print(dp[k])
