# 움직이는 미로 탈출

import sys
from collections import deque

input = sys.stdin.readline

wall = []
for y in range(8):
    row = input().strip()
    for x, w in enumerate(row):
        if w == "#":
            wall.append((y, x))

dy = (-1, -1, 0, 1, 1, 1, 0, -1, 0)
dx = (0, -1, -1, -1, 0, 1, 1, 1, 0)


def BFS(y, x):
    global wall

    q = deque()
    q.append((y, x))

    while q:
        for _ in range(len(q)):
            y, x = q.popleft()

            if (y, x) in wall:
                continue
            if (y, x) == (0, 7):
                return 1
            for i in range(9):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < 8 and 0 <= nx < 8 and not (ny, nx) in wall:
                    if ny == 0 and nx == 7:
                        return 1
                    q.append((ny, nx))

        new_wall = []
        for i, w in enumerate(wall):
            wall_y, wall_x = w[0], w[1]
            new_y = wall_y + 1
            if new_y > 7:
                continue
            else:
                new_wall.append((new_y, wall_x))
        wall = new_wall

    return 0


start_y, start_x = 7, 0
print(BFS(start_y, start_x))
