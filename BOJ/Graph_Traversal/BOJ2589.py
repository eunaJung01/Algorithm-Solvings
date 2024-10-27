# 보물섬

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
treasure_map = [input().strip() for _ in range(N)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(y, x):
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[y][x] = True
    q = deque()
    q.append((y, x, 0))
    cnt = 0

    while q:
        y, x, c = q.popleft()
        cnt = max(cnt, c)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and treasure_map[ny][nx] == "L" and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, c + 1))
    return cnt


result = 0
for y in range(N):
    for x in range(M):
        if treasure_map[y][x] == "L":
            result = max(result, BFS(y, x))

print(result)
