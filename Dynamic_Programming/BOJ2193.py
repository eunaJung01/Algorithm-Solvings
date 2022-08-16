# 이친수

import sys

N = int(sys.stdin.readline().strip())

result = 0
if N == 1 or N == 2:
    result = 1
elif N == 3:
    result = 2
else:
    ans = [0] * (N + 1)
    ans[1] = 1
    ans[2] = 1
    ans[3] = 2

    dp = [0] * (N + 1)
    dp[2] = 1
    dp[3] = 1

    for i in range(4, N + 1):
        dp[i] = dp[i - 2] + dp[i - 1]
        ans[i] = ans[i - 1] + dp[i - 1]

    result = ans[N]

print(result)
