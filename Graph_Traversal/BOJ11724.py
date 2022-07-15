# 연결 요소의 개수

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())  # 정점 N개, 간선 M개

graph = [[0 for _ in range(N)] for _ in range(N)]  # 노드 0번 ~ N-1번

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().split())
    n1 -= 1
    n2 -= 1
    graph[n1][n2] = 1
    graph[n2][n1] = 1

visited = [False for _ in range(N)]


def BFS(i):
    global graph
    global visited

    q = deque([])
    q.append(i)
    visited[i] = True

    while q:
        n = q.popleft()
        visited[n] = True
        for j in range(N):
            if graph[n][j] == 1:
                graph[n][j] = 0
                q.append(j)


result = 0

if M == 0:  # 간선이 없는 경우
    result = N
else:
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                result += 1
                BFS(i)

    for v in visited:  # 간선이 없는 노드 처리
        if not v:
            result += 1

print(result)
