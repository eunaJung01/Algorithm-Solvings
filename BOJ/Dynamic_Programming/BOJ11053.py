# 가장 긴 증가하는 부분 수열

import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().split()))

dp = [0] * N

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if line[j] < line[i] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))
