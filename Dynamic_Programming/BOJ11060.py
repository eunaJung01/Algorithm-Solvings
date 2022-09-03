# 점프 점프

import sys

N = int(sys.stdin.readline().strip())
jump = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(0)

else:
    dp = [999 for _ in range(N)]
    for i in range(jump[0]):
        dp[i + 1] = 1

    for i in range(1, N):
        for j in range(jump[i]):
            idx = i + j + 1
            if idx < N:
                dp[idx] = min(dp[idx], dp[i] + 1)

    if dp[N - 1] == 999:
        print(-1)
    else:
        print(dp[N - 1])
