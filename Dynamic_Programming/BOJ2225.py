# 합분해

# Python 3 - 52ms

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[1 for _ in range(N + 1)] for _ in range(K + 1)]
for i in range(2, K + 1):
    for j in range(1, N + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
print(dp[K][N])

# Python 3 - 48ms

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

dp = [1 for _ in range(K + 1)]
for _ in range(N):
    for j in range(2, K + 1):
        dp[j] = (dp[j - 1] + dp[j]) % 1000000000
print(dp[K])
