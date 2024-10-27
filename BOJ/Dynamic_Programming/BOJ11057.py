# 오르막 수

import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] += dp[i - 1][j]
            dp[i][k] %= 10007

result = 0
for i in range(10):
    result += dp[N][i]
print(result % 10007)
