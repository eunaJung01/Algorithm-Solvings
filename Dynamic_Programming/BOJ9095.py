# 1, 2, 3 더하기

import sys

dp = [0 for _ in range(11)]  # 방법의 수


def num(n):
    if n == 1 or n == 2:
        return n
    if n == 3:
        return 4

    if dp[n] != 0:
        return dp[n]

    dp[n] = num(n - 1) + num(n - 2) + num(n - 3)
    return dp[n]


T = int(sys.stdin.readline().strip())
case = []
for _ in range(T):
    case.append(int(sys.stdin.readline().strip()))

for c in case:
    print(num(c))
