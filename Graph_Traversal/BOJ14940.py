# 쉬운 최단거리

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ground = []

d_y, d_x = 0, 0
for y in range(n):
    line = list(map(int, input().split()))
    for x in range(m):
        if line[x] == 2:
            d_y, d_x = y, x
    ground.append(line)

dy = (0, 0, -1, 1)
dx = (-1, 1, 0, 0)
result = [[0 for _ in range(m)] for _ in range(n)]


def BFS(start_y, start_x):
    global visited, result

    q = deque()
    q.append((start_y, start_x))
    visited[start_y][start_x] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and ground[ny][nx] == 1:
                result[ny][nx] = result[y][x] + 1
                visited[ny][nx] = True
                q.append((ny, nx))


visited = [[False for _ in range(m)] for _ in range(n)]
BFS(d_y, d_x)

for y in range(n):
    for x in range(m):
        if ground[y][x] == 1 and not visited[y][x]:
            print(-1, end=' ')
        else:
            print(result[y][x], end=' ')
    print()
