# 피보나치 함수

import sys

dp = [(0, 0) for _ in range(42)]  # 0 출력 횟수, 1출력 횟수
dp[0] = (1, 0)
dp[1] = (0, 1)

T = int(sys.stdin.readline().strip())
case = [int(sys.stdin.readline().strip()) for _ in range(T)]

for i in range(2, max(case) + 1):
    dp[i] = (dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1])

for c in case:
    print(dp[c][0], dp[c][1])
