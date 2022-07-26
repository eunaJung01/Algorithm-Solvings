# 다리 놓기

import sys

dp = [[0] * 31 for _ in range(31)]

T = int(sys.stdin.readline().strip())
case = []
for _ in range(T):
    case.append(list(map(int, sys.stdin.readline().split())))


def combination(m, n):
    global dp

    if m == n or n == 0:
        return 1

    if dp[m][n] != 0:
        return dp[m][n]

    dp[m][n] = combination(m - 1, n) + combination(m - 1, n - 1)
    return dp[m][n]


for n, m in case:
    print(combination(m, n))
