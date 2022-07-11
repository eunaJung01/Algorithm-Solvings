# 미로 탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False for _ in range(M)] for _ in range(N)]

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)


def BFS(r, c):
    q = deque([])
    q.append([r, c])

    visited[r][c] = True

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                maze[ny][nx] = maze[y][x] + 1
                q.append([ny, nx])


BFS(0, 0)
print(maze[N - 1][M - 1])
