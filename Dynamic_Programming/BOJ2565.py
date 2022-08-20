# 전깃줄

import sys

N = int(sys.stdin.readline().strip())

line = []
for _ in range(N):
    line.append(list(map(int, sys.stdin.readline().split())))
line.sort()

dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = 1
    for j in range(1, i):
        if dp[i] <= dp[j] and line[i - 1][0] > line[j - 1][0] and line[i - 1][1] > line[j - 1][1]:
            dp[i] = dp[j] + 1

print(N - max(dp))
