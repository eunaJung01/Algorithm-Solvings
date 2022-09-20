# Four Squares

# 런타임 에러 (RecursionError)
# import sys
# sys.setrecursionlimit(10000)
#
# input = sys.stdin.readline
#
# n = int(input().strip())
#
# dp = [-1 for _ in range(n + 1)]
#
#
# def func(num):
#     if dp[num] != -1:
#         return dp[num]
#
#     if num == 0 or num == 1:
#         dp[num] = num
#
#     else:
#         minValue = 50001
#         i = 1
#         while i * i <= num:
#             minValue = min(minValue, func(num - i * i))
#             i += 1
#         dp[num] = minValue + 1
#
#     return dp[num]
#
#
# print(func(n))

# ---

import sys

N = int(sys.stdin.readline().strip())
dp = [0, 1]

for i in range(2, N + 1):
    minValue = 1e9
    j = 1
    while j ** 2 <= i:
        minValue = min(minValue, dp[i - (j ** 2)])
        j += 1
    dp.append(minValue + 1)

print(dp[N])
