# 양

import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().split())
yard = [list(input().strip()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def BFS(start_y, start_x):
    global visited, sheep_survived, wolves_survived

    sheep, wolf = 0, 0
    if yard[start_y][start_x] == "v":
        wolf += 1
    elif yard[start_y][start_x] == "o":
        sheep += 1

    visited[start_y][start_x] = True
    q = deque()
    q.append((start_y, start_x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C and yard[y][x] != "#" and not visited[ny][nx]:
                visited[ny][nx] = True
                if yard[ny][nx] == "v":
                    wolf += 1
                elif yard[ny][nx] == "o":
                    sheep += 1
                q.append((ny, nx))

    if sheep > wolf:
        sheep_survived += sheep
    else:
        wolves_survived += wolf


sheep_survived, wolves_survived = 0, 0
for y in range(R):
    for x in range(C):
        if yard[y][x] != "#" and not visited[y][x]:
            BFS(y, x)
print(sheep_survived, wolves_survived)
