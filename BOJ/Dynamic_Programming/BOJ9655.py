# 돌 게임

import sys
import math

dp = [0 for _ in range(1001)]  # 게임 횟수를 저장


def game(N):
    if N == 1 or N == 3:
        return 1
    if dp[N] != 0:
        return dp[N]

    dp[N] = game(N // 2) + game(int(math.ceil(N / 2)))
    return dp[N]


N = int(sys.stdin.readline().strip())
if game(N) % 2 == 0:
    print("CY")
else:
    print("SK")
