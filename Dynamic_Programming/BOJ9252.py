# LCS 2

import sys

input = sys.stdin.readline

str1, str2, = input().strip(), input().strip()
N, M = len(str1), len(str2)
dp = [[[0, ""] for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = [dp[i - 1][j - 1][0] + 1, dp[i - 1][j - 1][1] + str1[i - 1]]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[N][M][0])
print(dp[N][M][1])
