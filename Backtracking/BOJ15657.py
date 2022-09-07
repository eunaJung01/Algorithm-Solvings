# N과 M (8)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))
arr = []


def func(idx, cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return
    for i in range(idx, N):
        arr.append(numList[i])
        func(i, cnt + 1)
        arr.pop()


func(0, 0)
