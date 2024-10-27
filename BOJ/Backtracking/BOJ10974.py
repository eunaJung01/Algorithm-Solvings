# 모든 순열

import sys

N = int(sys.stdin.readline())
status = [False for _ in range(N)]
num = []


def func(cnt):
    if cnt == N:
        for n in num:
            print(n, end=' ')
        print()
        return

    for i in range(N):
        if not status[i]:
            status[i] = True
            num.append(i + 1)
            func(cnt + 1)
            status[i] = False
            num.pop()


func(0)
