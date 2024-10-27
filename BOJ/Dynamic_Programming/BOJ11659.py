# 구간 합 구하기 4

import sys

M, N = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0 for _ in range(M + 1)]
for i in range(1, M + 1):
    dp[i] = dp[i - 1] + num[i - 1]

for a, b in lst:
    print(dp[b] - dp[a - 1])
