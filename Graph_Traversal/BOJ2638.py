# 치즈

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(y, x):
    global visited, air

    isAir = False
    temp = [(y, x)]
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and cheese[ny][nx] == 0:
                visited[ny][nx] = True
                if ny == 0 or ny == N - 1 or nx == 0 or nx == M - 1:
                    isAir = True
                temp.append((ny, nx))
                q.append((ny, nx))

    if isAir:
        for y, x in temp:
            air[y][x] = True


result = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    air = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    c = []

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if cheese[i][j] == 1:
                    visited[i][j] = True
                    c.append((i, j))
                    cnt += 1
                else:
                    BFS(i, j)

    if cnt == 0:
        break
    else:
        result += 1
        for y, x in c:
            airCnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < M and air[ny][nx]:
                    airCnt += 1
                    if airCnt >= 2:
                        cheese[y][x] = 0
                        break

print(result)
