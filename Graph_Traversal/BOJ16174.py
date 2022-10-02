# 점프왕 쩰리 (Large)

import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
game = [list(map(int, input().split())) for _ in range(N)]

dy = (1, 0)
dx = (0, 1)

status = [[False for _ in range(N)] for _ in range(N)]


def BFS(y, x):
    result = False
    status[0][0] = True

    q = deque()
    q.append((y, x))

    while q:
        if result:
            break
        else:
            y, x = q.popleft()
            for i in range(2):
                ny = y + dy[i] * game[y][x]
                nx = x + dx[i] * game[y][x]
                if 0 <= ny < N and 0 <= nx < N and not status[ny][nx]:
                    if ny == N - 1 and nx == N - 1:
                        result = True
                    status[ny][nx] = True
                    q.append((ny, nx))
    return result


result = BFS(0, 0)
if result:
    print("HaruHaru")
else:
    print("Hing")
