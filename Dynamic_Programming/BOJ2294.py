# 동전 2

import sys

n, k = map(int, sys.stdin.readline().split())
price = [int(sys.stdin.readline().strip()) for _ in range(n)]

dp = [0 for _ in range(k + 1)]

for i in range(1, k + 1):
    temp = []
    for j in price:
        if j <= i and dp[i - j] != -1:
            temp.append(dp[i - j])
    if not temp:
        dp[i] = -1
    else:
        dp[i] = min(temp) + 1

print(dp[k])
