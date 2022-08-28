# N과 M (4)

import sys

N, M = map(int, sys.stdin.readline().split())

arr = [0 for _ in range(M + 1)]


def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()

    for i in range(1, N + 1):
        if k < M and arr[k - 1] <= i:
            arr[k] = i
            func(k + 1)


func(0)
