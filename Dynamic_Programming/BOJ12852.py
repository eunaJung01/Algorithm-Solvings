# 1로 만들기 2

import sys

N = int(sys.stdin.readline().strip())

if N == 1:
    print(0)
    print(1)
else:
    dp = [[0 for _ in range(N + 1)] for _ in range(2)]

    for i in range(2, N + 1):
        if i == 2 or i == 3:
            dp[0][i] = 1
            dp[1][i] = 1

        dp[0][i] = dp[0][i - 1] + 1
        dp[1][i] = i - 1

        if i % 3 == 0 and dp[0][i // 3] < dp[0][i]:
            dp[0][i] = dp[0][i // 3] + 1
            dp[1][i] = i // 3

        if i % 2 == 0 and dp[0][i // 2] < dp[0][i]:
            dp[0][i] = dp[0][i // 2] + 1
            dp[1][i] = i // 2

    print(dp[0][N])

    while N != 1:
        print(N, end=' ')
        N = dp[1][N]
    print(1)
