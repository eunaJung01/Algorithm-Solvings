# 엽속합 2

import sys

input = sys.stdin.readline

n = int(input().strip())
num = list(map(int, input().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(2)]
dp[0][0] = num[0]
dp[1][0] = num[0]
result = num[0]

for i in range(1, n):
    dp[0][i] = max(0, dp[0][i - 1]) + num[i]
    dp[1][i] = max(dp[1][i - 1] + num[i], dp[0][i - 1])
    result = max(result, max(dp[0][i], dp[1][i]))

print(result)
