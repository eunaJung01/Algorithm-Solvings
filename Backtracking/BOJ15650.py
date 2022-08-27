# N과 M (2)

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(10)]
status = [False for _ in range(10)]


def func(k):
    global status

    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not status[i] and arr[k - 1] < i:
            arr[k] = i
            status[i] = True
            func(k + 1)
            status[i] = False


func(0)
