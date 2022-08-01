# 2xn 타일링 2

import sys

dp = [0 for _ in range(1001)]  # n -> 타일 채우는 방법의 수


def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    if dp[n] != 0:
        return dp[n]

    dp[n] = tile(n - 1) + tile(n - 2) * 2
    return dp[n]


n = int(sys.stdin.readline().strip())
print(tile(n) % 10007)
