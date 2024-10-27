# 과제

import sys

input = sys.stdin.readline

N = int(input().strip())

tasks = []
for _ in range(N):
    d, w = map(int, input().split())
    tasks.append((w, d))
tasks.sort(reverse=True)

dailyTasks = [0 for _ in range(1001)]
for score, deadline in tasks:
    if dailyTasks[deadline] == 0:
        dailyTasks[deadline] = score
    else:
        while deadline != 1:
            deadline -= 1
            if dailyTasks[deadline] == 0:
                dailyTasks[deadline] = score
                break

print(sum(dailyTasks))
