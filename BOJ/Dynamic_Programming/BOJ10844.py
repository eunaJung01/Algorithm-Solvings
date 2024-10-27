# 쉬운 계단 수

import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        for j in range(1, 10):
            dp[i][j] = 1
        continue

    for j in range(10):
        if j == 0:
            dp[i][j] = (dp[i - 1][j + 1]) % 1000000000
        elif j == 9:
            dp[i][j] = (dp[i - 1][j - 1]) % 1000000000
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % 1000000000

result = 0
for j in range(10):
    result += dp[N][j]
print(result % 1000000000)
