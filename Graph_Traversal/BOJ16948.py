# 데스 나이트

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
r1, c1, r2, c2 = map(int, input().split())

dy = (-2, -2, 0, 0, 2, 2)
dx = (-1, 1, -2, 2, -1, 1)

visited = [[False for _ in range(N)] for _ in range(N)]


def BFS(y, x):
    visited[y][x] = False
    q = deque()
    q.append((y, x, 0))

    while q:
        y, x, num = q.popleft()
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if ny == r2 and nx == c2:
                    return num + 1
                visited[ny][nx] = True
                q.append((ny, nx, num + 1))
    return -1


print(BFS(r1, c1))
