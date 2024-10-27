# N과 M (11)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()

arr = []


def func(cnt):
    if cnt == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    temp = 0
    for i in range(N):
        if temp != numList[i]:
            temp = numList[i]
            arr.append(numList[i])
            func(cnt + 1)
            arr.pop()


func(0)
