# 상자넣기

import sys

n = int(sys.stdin.readline().strip())
box = list(map(int, sys.stdin.readline().split()))
result = 0

if n == 1:
    result = 1

else:
    dp = [0 for _ in range(n)]
    dp[0] = 1

    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if box[j] < box[i] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1

    result = max(dp)

print(result)
