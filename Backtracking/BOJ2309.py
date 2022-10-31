# 일곱 난쟁이

import copy
import sys

input = sys.stdin.readline

height = [int(input().strip()) for _ in range(9)]
height.sort()

status = [False for _ in range(9)]
check = False
arr = []


def func(cnt):
    global check
    global arr

    if check:
        return

    if cnt == 7:
        temp = 0
        for i in range(9):
            if status[i]:
                temp += height[i]
        if temp == 100:
            check = True
            arr = copy.deepcopy(status)
        return

    for i in range(9):
        if not status[i]:
            status[i] = True
            func(cnt + 1)
            status[i] = False
            if check:
                return


func(0)

result = []
for i in range(9):
    if arr[i]:
        result.append(height[i])

for r in result:
    print(r)
