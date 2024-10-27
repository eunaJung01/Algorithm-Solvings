# 파도반 수열

import sys

T = int(sys.stdin.readline().strip())
P = [int(sys.stdin.readline().strip()) for _ in range(T)]

dp = [0, 1, 1, 1, 2, 2, 3, 4, 5]

if max(P) > len(dp):
    for i in range(len(dp), max(P) + 1):
        dp.append(dp[i - 5] + dp[i - 1])

for p in P:
    print(dp[p])
