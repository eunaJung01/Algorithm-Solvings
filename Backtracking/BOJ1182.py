# 부분수열의 합

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
numList = list(map(int, input().split()))

result = 0


def DFS(i, total):
    global result

    if total == S:
        result += 1

    for j in range(i + 1, N):
        DFS(j, total + numList[j])


for i in range(N):
    DFS(i, numList[i])

print(result)
