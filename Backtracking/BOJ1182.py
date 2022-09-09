# 부분수열의 합

import sys

input = sys.stdin.readline
N, S = map(int, input().split())
numList = list(map(int, input().split()))

status = [False for _ in range(N)]
result = 0


def DFS(i, graph, total):
    global result

    if total == S:
        result += 1

    for j in range(i + 1, N):
        DFS(j, graph, total + graph[j])


for i in range(N):
    DFS(i, numList, numList[i])

print(result)
