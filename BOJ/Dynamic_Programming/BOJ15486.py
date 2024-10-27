# 퇴사 2

# 시간 초과
# import sys
#
# N = int(sys.stdin.readline().strip())
#
# profit = []  # i번 상담을 했을 때 얻을 수 있는 이익
# c = [[] for _ in range(N + 1)]  # x일까지 가능한 상담의 번호(i)
#
# for i in range(N):
#     day, p = map(int, sys.stdin.readline().split())  # 상담 시 걸리는 날짜, 이익
#     if i + day <= N:
#         c[i + day].append(i)
#         profit.append(p)
#     else:
#         profit.append(0)
#
# print(profit)
# print(c)
#
# dp = [0 for _ in range(N + 1)]
# for i in range(N + 1):
#     if len(c[i]) == 0:
#         dp[i] = max(dp)
#     else:
#         temp = 0
#         for j in range(len(c[i])):
#             temp = max(temp, profit[c[i][j]] + dp[c[i][j]])
#         dp[i] = temp
#
# print(dp)
# print(max(dp))

# ---

import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 1)]

for i in range(N):
    d, p = map(int, sys.stdin.readline().split())  # 상담 시 걸리는 날짜, 이익
    dp[i] = max(dp[i - 1], dp[i])
    if i + d <= N:
        dp[i + d] = max(dp[i + d], p + dp[i])

print(max(dp))
