# 2xn 타일링

import sys

dp = [0 for _ in range(1001)]  # n -> 타일 채우는 방법의 수


def tile(n):
    if n == 1 or n == 2:
        return n
    if dp[n] != 0:
        return dp[n]

    dp[n] = tile(n - 1) + tile(n - 2)
    return dp[n]


n = int(sys.stdin.readline().strip())
print(tile(n) % 10007)
