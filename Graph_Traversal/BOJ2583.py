# 영역 구하기

import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def BFS(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 1
    size = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                q.append((ny, nx))
                size += 1
    return size


result = []
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            result.append(BFS(i, j))

result.sort()
print(len(result))
for r in result:
    print(r, end=' ')
