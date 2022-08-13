# 정수 삼각형

import sys

n = int(sys.stdin.readline().strip())
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(1, len(line) + 1):
        dp[i][j] = line[j - 1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))
