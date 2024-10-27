# 집합

import sys

M = int(sys.stdin.readline().strip())
lst = [False for _ in range(21)]

for _ in range(M):
    line = sys.stdin.readline().strip()

    if line == "empty":
        for i in range(21):
            if lst[i]:
                lst[i] = False
    elif line == "all":
        for i in range(21):
            if not lst[i]:
                lst[i] = True

    else:
        inst, num = line.split()
        num = int(num) - 1

        if inst == "add":
            if not lst[num]:
                lst[num] = True

        elif inst == "remove":
            if lst[num]:
                lst[num] = False

        elif inst == "check":
            if lst[num]:
                print(1)
            else:
                print(0)

        elif inst == "toggle":
            if lst[num]:
                lst[num] = False
            else:
                lst[num] = True
