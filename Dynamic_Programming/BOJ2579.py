# 계단 오르기

import sys

n = int(sys.stdin.readline().strip())
stair = [int(sys.stdin.readline().strip()) for _ in range(n)]

result = 0

if n == 1 or n == 2:
    result = sum(stair)
else:
    dp = [0 for _ in range(n)]
    dp[0] = stair[0]
    dp[1] = stair[1]
    dp[2] = stair[2]

    for i in range(3, n - 1):
        dp[i] = min(dp[i - 2], dp[i - 3]) + stair[i]

    result = sum(stair) - min(dp[n - 3], dp[n - 2])

print(result)
