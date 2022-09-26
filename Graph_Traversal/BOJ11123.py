# 양 한마리... 양 두마리...

import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())
result = []

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(H, W, y, x):
    global status

    q = deque()
    q.append((y, x))
    status[y][x] = True

    while q:
        y, x = q.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < H and 0 <= nx < W and not status[ny][nx] and grid[ny][nx] == 1:
                status[ny][nx] = True
                q.append((ny, nx))


for _ in range(T):
    H, W = map(int, input().split())
    status = [[False for _ in range(W)] for _ in range(H)]

    grid = []
    for _ in range(H):
        line = input().strip()
        temp = []
        for l in line:
            if l == ".":
                temp.append(0)
            else:
                temp.append(1)
        grid.append(temp)

    r = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 1 and not status[i][j]:
                BFS(H, W, i, j)
                r += 1
    result.append(r)

for r in result:
    print(r)
