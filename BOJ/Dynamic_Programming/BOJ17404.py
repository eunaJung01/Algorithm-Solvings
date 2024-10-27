# RGB거리 2

import sys

N = int(sys.stdin.readline().strip())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = 9999999

if N == 2:
    for i in range(3):
        result = min(result, min(RGB[0][i - 1], RGB[0][i - 2]) + RGB[1][i])

else:
    # 첫번째 집 1. R / 2. G / 3. B
    idx = [[1, 2], [2, 0], [0, 1]]  # 두번째 집 & N번째 집

    for k in range(3):  # 첫번째 집 0, 1, 2
        dp = [[9999999 for _ in range(N - 1)] for _ in range(3)]
        for i in range(3):
            dp[i][0] = RGB[0][i]

        for i in range(1, N):
            if i == 1:
                for j in range(2):
                    dp[idx[k][j]][i] = dp[k][i - 1] + RGB[i][idx[k][j]]
                continue

            if i == N - 1:
                for j in range(2):
                    result = min(result, min(dp[idx[k][j] - 1][i - 1], dp[idx[k][j] - 2][i - 1]) + RGB[i][idx[k][j]])
                continue

            for j in range(3):
                dp[j][i] = min(dp[j - 1][i - 1], dp[j - 2][i - 1]) + RGB[i][j]

print(result)
