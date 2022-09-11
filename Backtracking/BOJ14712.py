# 넴모넴모 (Easy)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

result = 0
status = [[False for _ in range(M + 1)] for _ in range(N + 1)]


def DFS(y, x):
    global result, status

    if (y, x) == (N + 1, 1):
        result += 1
        return

    if x == M:
        ny, nx = y + 1, 1
    else:
        ny, nx = y, x + 1

    # (y, x)에 네모를 놓지 않는 경우
    DFS(ny, nx)

    # (y, x)에 네모를 놓는 경우
    if not status[y - 1][x] or not status[y - 1][x - 1] or not status[y][x - 1]:
        status[y][x] = True
        DFS(ny, nx)
        status[y][x] = False


DFS(1, 1)
print(result)
