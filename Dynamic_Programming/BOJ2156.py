# 포도주 시식

import sys

n = int(sys.stdin.readline().strip())
wine = [int(sys.stdin.readline().strip()) for _ in range(n)]

result = 0
if n == 1 or n == 2:
    result = sum(wine)
else:
    dp = [0 for _ in range(n)]
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

    result = dp[n - 1]

print(result)
