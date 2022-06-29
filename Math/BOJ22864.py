# 피로도

import sys

A, B, C, M = map(int, sys.stdin.readline().split())

# if A >= M:
#     work_time = 0
# else:
#     work_time = int((M + 24 * C) / (A + C))  # A*work_time - (24-work_time)*C = M
#
# print(work_time * B)

time = 0  # 현재 시간
work_time = 0  # 일한 시간
fatigue = 0  # 피로도

while time < 24:
    if fatigue + A <= M:
        work_time += 1
        fatigue += A
    else:
        fatigue -= C
        if fatigue < 0:
            fatigue = 0
    time += 1

print(work_time * B)
