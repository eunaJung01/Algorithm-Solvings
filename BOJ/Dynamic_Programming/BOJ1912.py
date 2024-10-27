# 연속합

import sys

n = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().split()))

num = [line[0]]
for i in range(1, n):
    num.append(num[i - 1] + line[i])

dp = [0] * n
dp[0] = num[0]

m = num[0]
for i in range(1, n):
    dp[i] = max(num[i], num[i] - m, line[i])
    if num[i] < m:
        m = num[i]

print(max(dp))
