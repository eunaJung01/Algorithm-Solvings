# 설탕 배달

import sys

dp = [0 for _ in range(5001)]
dp[3] = 1
dp[5] = 1

N = int(sys.stdin.readline().strip())
for i in range(6, N + 1):
    if i % 5 == 0:
        dp[i] = dp[i - 5] + 1
    elif i % 3 == 0:
        dp[i] = dp[i - 3] + 1
    else:
        if dp[i - 3] != 0 and dp[i - 5] != 0:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])
