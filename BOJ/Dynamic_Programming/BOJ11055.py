# 가장 큰 증가 부분 수열

import sys

N = int(sys.stdin.readline().strip())
line = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * N  # 연속
dp2 = [0] * N  # 합

for i in range(N):
    dp1[i] = 1
    dp2[i] = line[i]
    temp = []
    for j in range(i):
        if line[j] < line[i] and dp1[i] <= dp1[j]:
            dp1[i] = dp1[j] + 1
            temp.append(dp2[j])
    if temp:
        dp2[i] += max(temp)

print(max(dp2))
