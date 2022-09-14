# 트리의 부모 찾기

import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = [0] * (N + 1)


def DFS(n):
    if n == N + 2:
        return

    for i in graph[n]:
        if result[i] == 0:
            result[i] = n
            DFS(i)


DFS(1)
for i in range(2, N + 1):
    print(result[i])
