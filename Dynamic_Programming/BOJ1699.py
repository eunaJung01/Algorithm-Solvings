# 제곱수의 합

import sys
from math import sqrt

input = sys.stdin.readline

N = int(input().strip())

dp = [100000 for _ in range(N + 1)]
for i in range(1, int(sqrt(N)) + 1):
    dp[i ** 2] = 1

if dp[N] == 1:
    print(1)
else:
    for i in range(1, N + 1):
        if dp[i] == 1:
            j = 1
            while True:
                if i + j > N:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + dp[j])
                j += 1
    print(dp[N])
