# 가장 긴 감소하는 부분 수열

import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N)]

for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] > A[i] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

print(max(dp))
