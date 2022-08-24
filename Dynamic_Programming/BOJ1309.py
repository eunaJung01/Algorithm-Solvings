# 동물원

import sys

N = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(N + 1)] for _ in range(2)]  # 공백 / 왼쪽 or 오른쪽
for i in range(2):
    dp[i][1] = 1

for i in range(2, N + 1):
    dp[0][i] = (dp[0][i - 1] + dp[1][i - 1] * 2) % 9901
    dp[1][i] = (dp[0][i - 1] + dp[1][i - 1]) % 9901

result = (dp[0][N] + dp[1][N] * 2) % 9901
print(result)
