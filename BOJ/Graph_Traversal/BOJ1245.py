# 농장 관리

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dy = (-1, 1, 0, 0, 1, 1, -1, -1)
dx = (0, 0, -1, 1, 1, -1, 1, -1)


def DFS(y, x):
    global visited, status

    visited[y][x] = True

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if map[y][x] < map[ny][nx]:
                status = False
            if not visited[ny][nx] and map[y][x] == map[ny][nx]:
                visited[ny][nx] = True
                DFS(ny, nx)


result = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == 0:
            visited[i][j] = True
            continue
        if not visited[i][j] and map[i][j] != 0:
            status = True
            DFS(i, j)
            if status:
                result += 1
print(result)
