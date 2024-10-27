# N과 M (5)

import sys

N, M = map(int, sys.stdin.readline().split())

numList = [0]
temp = list(map(int, sys.stdin.readline().split()))
for t in temp:
    numList.append(t)
numList.sort()

arr = [0 for _ in range(M + 1)]
status = [False for _ in range(N + 1)]


def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()

    for i in range(1, N + 1):
        if k < M and not status[i]:
            arr[k] = numList[i]
            status[i] = True
            func(k + 1)
            status[i] = False


func(0)
