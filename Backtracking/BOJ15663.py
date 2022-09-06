# N과 M (9)

import sys

N, M = map(int, sys.stdin.readline().split())

numList = list(map(int, sys.stdin.readline().split()))
numList.sort()

arr = [0 for _ in range(M)]
status = [False for _ in range(N)]


def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    temp = 0
    for i in range(N):
        if not status[i] and temp != numList[i]:
            arr[k] = numList[i]
            temp = numList[i]
            status[i] = True
            func(k + 1)
            status[i] = False


func(0)
