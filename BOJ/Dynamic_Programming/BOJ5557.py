# 1학년

import sys

input = sys.stdin.readline

N = int(input().strip())
numbers = list(map(int, input().split()))

# dp[i번째][현재까지의 수] = 가능한 경우의 수
dp = [[0 for _ in range(21)] for _ in range(N - 1)]
dp[0][numbers[0]] = 1

for i in range(1, N - 1):
    for j in range(21):
        if dp[i - 1][j] > 0:
            if j + numbers[i] <= 20:
                dp[i][j + numbers[i]] += dp[i - 1][j]
            if j - numbers[i] >= 0:
                dp[i][j - numbers[i]] += dp[i - 1][j]

print(dp[N - 2][numbers[N - 1]])
